"""mall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# import xadmin
from django.conf.urls import url, include
# from django.contrib import admin
from verifications import views

urlpatterns = [

    # url(r'^admin/', admin.site.urls),

    # url(r'^admin/', admin.site.urls),

    # url(r'xadmin/', include(xadmin.site.urls)),

    # url(r'^admin/', admin.site.urls),
    # url(r'xadmin/', include(xadmin.site.urls)),

    # url(r'^users/',include('users.urls',namespace='users')),
    url(r'^verifications/',include('verifications.urls',namespace='verifications')),
    url(r'^oauth/',include('oauth.urls',namespace='oauth')),
    url(r'^areas/',include('areas.urls',namespace='areas')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^goods/', include('goods.urls', namespace='goods')),
    url(r'^cart/', include('carts.urls', namespace='carts')),
    url(r'^orders/', include('orders.urls', namespace='orders')),
    url(r'^skus/', include('orders.urls')),
    url(r'^pay/', include('pay.urls', namespace='pay')),

    #忘记密码
    # /accounts/13520204631/sms/token/?text=byh1&image_code_id=40353f31-d524-4439-a34b-7aa105b8020c HTTP/1.1" 404 3061
    url(r'^accounts/(?P<user_name>\w+)/sms/token/$',views.AccountsCaptchaView.as_view()),
    # /sms_codes/?access_token=
    url(r'^sms_codes/$',views.AccountsSMSCodeView.as_view()),
    # http://192.168.35.30:8000/accounts/13520204631/password/token/?sms_code=700786
    url(r'^accounts/(?P<user_name>\w+)/password/token/$',views.AccountsRevSMSView.as_view()),
    # /users/'+ this.user_id +'/password/
    url(r'^users/(?P<pk>\d+)/password/$',views.ResetPasswordView.as_view())

]
