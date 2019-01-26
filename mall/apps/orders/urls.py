# Author Caozy
from django.conf.urls import url

from orders import views

urlpatterns=[
    url('^places/$',views.OrderSettlementView.as_view(),name='placeorder'),# 订单页查询
    url('^$',views.OrderView.as_view(),name='commitorder'),# 订单提交
    url(r'^(?P<order_id>\d+)/uncommentgoods/$', views.ScoreOrderView.as_view()),
    url(r'^(?P<order_id>\d+)/comments/$', views.CommentView.as_view()),
    url(r'^(?P<sku_id>\d+)/comment/$', views.CommentsView.as_view())
    #http://192.168.107.128:8000/skus/1/comments/


]
