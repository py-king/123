from decimal import Decimal

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django_redis import get_redis_connection

from goods.models import SKU

from orders.models import OrderGoods
from orders.serializers import  ScoreOrderSerializer, CommentSerializer

from orders.serializers import OrderSettlementSerializer, OrderCommitSerializer, \
    OrderQuerySerializer



class OrderSettlementView(APIView):
    """订单结算视图"""
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user=request.user
        #redis中获取购物车信息
        redis_conn=get_redis_connection('cart')
        # 获取当前用户购物车信息
        redis_carts=redis_conn.hgetall('cart_%s'%user.id)
        carts_selected=redis_conn.smembers('cart_selected_%s'%user.id)
        # 获取选中的商品信息
        # 方式一
        # order_cart={}
        # for sku_id,count in redis_carts.items():
        #     if sku_id in carts_selected:
        #         order_cart[int(sku_id)]=int(count)
        # skus=SKU.objects.filter(id__in=[int(skuid) for skuid in carts_selected])
        # for sku in skus:
        #     sku.count=order_cart[sku.id]
        # 方式二
        order_cart = {}
        for sku_id in carts_selected:
            order_cart[int(sku_id)]=int(redis_carts[sku_id])
        skus=SKU.objects.filter(id__in=order_cart.keys())
        for sku in skus:
            sku.count=order_cart[sku.id]

        freight = Decimal('10.00')
        serializer=OrderSettlementSerializer({'freight':freight,'skus':skus})
        return Response(serializer.data)

from rest_framework.generics import CreateAPIView,ListAPIView




class ScoreOrderView(APIView):
    def get(self,request,order_id):
        skus =OrderGoods.objects.filter(order_id__exact=order_id)
        print(skus)
        serializers =  ScoreOrderSerializer(skus,many=True)
        return Response(serializers.data)


class CommentView(APIView):
    def post(self,request,order_id):
        data = request.data
        del data['order']
        data1 = data
        skus = OrderGoods.objects.filter(order_id__exact=order_id,sku_id__exact=data['sku'])
        for sku in skus:
            serilaizers = CommentSerializer(sku,data1)
            serilaizers.is_valid()
            serilaizers.save()
            return Response({'msg': 'ok'})


class OrderView(CreateAPIView, ListAPIView):
    '''订单提交视图'''
    permission_classes = [IsAuthenticated]
    serializer_class = OrderCommitSerializer
    def get_serializer_class(self):
        if self.request.method=='POST':
            return OrderCommitSerializer
        else:
            return OrderQuerySerializer

    def get_queryset(self):
        '''
        订单列表：GET /orders/?page=1&page_size=5
        1.接收请求
        2.查询数据：订单编号、订单时间、商品id、商品名称、商品金额、商品数量、商品总金额、订单状态
        3.返回数据
        '''
        user = self.request.user
        from orders.models import OrderInfo, OrderGoods
        orderinfos = OrderInfo.objects.filter(user_id=user.id).order_by('-create_time')  # 订单集
        for orderinfo in orderinfos:
            skus = OrderGoods.objects.filter(order=orderinfo)  # 订单商品集
            orderinfo.skus = skus
            return orderinfos

