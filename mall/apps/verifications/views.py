from random import randint

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView

from users.models import User
from verifications.serializers import RegisterSMSCodeSerializer, AccountsRevSMSServializer, ResetPasswordSerializer
from rest_framework import status
from rest_framework.response import Response
from libs.captcha.captcha import captcha #导入验证码生成模块
from django_redis import get_redis_connection
from libs.yuntongxun.sms import CCP


class RegisterCaptchaView(APIView):
    '''
    图形验证码生成
    http://127.0.0.1:8000/verifications/imagecodes/image_code_id/
    '''
    def get(self,request,image_code_id):
        if not image_code_id:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        code_id,text,image=captcha.generate_captcha() #获取验证码
        print('image_code:',text)
        #保存uuid_code和image_code_id对应存储到redis中
        redis_conn=get_redis_connection('code')
        redis_conn.setex('img_%s'%image_code_id,60,text)
        #返回给前段image_text图片
        return HttpResponse(image,content_type='image/jpeg')

class RegisterSMSCodeView(GenericAPIView):
    '''
    短信验证码
    http://127.0.0.1:8000/verifications/smscodes/mobile/?text=xxx&image_code_id=xxx
    '''
    serializer_class = RegisterSMSCodeSerializer


    def get(self,request,mobile):
        #接收参数，验证参数
        serializer=self.get_serializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        redis_conn=get_redis_connection('code')
        if redis_conn.get('sms_flag_%s'%mobile): #是否频繁获取
           return Response(status=status.HTTP_429_TOO_MANY_REQUESTS)
        sms_code='%06d'%randint(0,999999)
        print('sms_code:',sms_code)
        redis_conn.setex('sms_%s'%mobile,5*60,sms_code)
        redis_conn.setex('sms_flag_%s'%mobile,60,1)

        # result=CCP().send_template_sms(mobile, ['sms_code', 5], 1)
        from celery_tasks.sms.tasks import send_sms_code
        send_sms_code.delay(mobile,sms_code)
        return Response({'message':'ok'})


class AccountsCaptchaView(APIView):
    '''获取图片验证码'''
    def get(self,request,user_name):
        params=request.query_params
        try:
            user=User.objects.filter(Q(username=user_name)|Q(mobile=user_name)).first()
        except User.DoesNotExist:
            raise Exception('用户不存在')

        serializer=RegisterSMSCodeSerializer(data=params,many=True)
        serializer.is_valid(raise_exception=True)

        # from utils.token_jwt import token_jwt
        # token = token_jwt(user)
        from .utils import generic_to_token
        token=generic_to_token(user.id)

        response = Response({
            'access_token': token,
            'mobile':user.mobile
        })
        return response

class AccountsSMSCodeView(APIView):
    '''获取手机验证码'''
    def get(self,request):
        params=request.query_params
        access_token=params.get('access_token')
        from .utils import check_access_token
        user_id=check_access_token(access_token)
        try:
            user=User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise Exception('用户不存在')

        redis_conn = get_redis_connection('code')
        if redis_conn.get('sms_flag_%s' % user.mobile):  # 是否频繁获取
            return Response(status=status.HTTP_429_TOO_MANY_REQUESTS)
        sms_code = '%06d' % randint(0, 999999)
        print('sms_code:', sms_code)
        redis_conn.setex('sms_%s' % user.mobile, 5 * 60, sms_code)
        redis_conn.setex('sms_flag_%s' % user.mobile, 60, 1)

        # result=CCP().send_template_sms(mobile, ['sms_code', 5], 1)
        from celery_tasks.sms.tasks import send_sms_code
        send_sms_code.delay(user.mobile, sms_code)
        return Response({'message': 'ok'})

class AccountsRevSMSView(APIView):
    '''
        get # http://192.168.35.30:8000/accounts/13520204631/password/token/?sms_code=700786
    '''
    def get(self,request,user_name):

        params=request.query_params
        sms_code=params['sms_code']
        data=[{'sms_code':sms_code,'user_name':user_name}]

        if user_name is not None:
            serializer=AccountsRevSMSServializer(data=data,many=True)
            serializer.is_valid(raise_exception=True)
            print(serializer.validated_data)
            return Response(serializer.validated_data)

from rest_framework.generics import UpdateAPIView
class ResetPasswordView(UpdateAPIView):
    '''重置密码'''
    def get_queryset(self):
        user_id = self.kwargs['pk']
        return User.objects.filter(id=user_id)
    serializer_class = ResetPasswordSerializer
