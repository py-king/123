#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:caozy time:19-1-10
from django_redis import get_redis_connection
from rest_framework import serializers

from oauth.models import OAuthQQUser, OAuthSinaUser
from oauth.utils import check_access_token
from users.models import User


class QQAuthUserSerializer(serializers.Serializer):
    '''
    QQ登录创建用户序列化器
    用于绑定openid和账户
    1.openid
    2.手机号
    3.密码
    4.手机验证码
    '''
    access_token = serializers.CharField(label='操作凭证')
    mobile = serializers.RegexField(label='手机号', regex=r'^1[3-9]\d{9}$')
    password = serializers.CharField(label='密码', max_length=20, min_length=8)
    sms_code = serializers.CharField(label='短信验证码')

    def validate(self, attrs):
        access_token=attrs.get('access_token')
        openid=check_access_token(access_token)
        if not openid:
            raise serializers.ValidationError('openid is error')
        attrs['openid']=openid # 用attrs传递数据

        #验证mobile/sms_code
        mobile=attrs.get('mobile')
        sms_code=attrs.get('sms_code')
        redis_conn=get_redis_connection('code')
        redis_sms_code=redis_conn.get('sms_%s'%mobile)
        # 验证码校验
        if not redis_sms_code:
            raise serializers.ValidationError('验证码过期')
        if redis_sms_code.decode()!=sms_code:
            raise serializers.ValidationError('验证码一致')
        try:
            user=User.objects.get(mobile=mobile)
        except User.DoesNotExist:
            # 没有注册需要执行注册
            pass
        else:
            # 说明注册过
            if not user.check_password(attrs.get('password')):
                raise serializers.ValidationError('的密码不正确')
            attrs['user']=user
        return attrs

    def create(self, validated_data):
        user=validated_data.get('user')
        if not user:
            user=User.objects.create(
                username=validated_data.get('mobile'),
                mobile=validated_data.get('mobile'),
                password=validated_data.get('password'),
            )
            user.set_password(validated_data.get('password'))
            user.save()
        qquser=OAuthQQUser.objects.create(
            openid=validated_data['openid'],
            user=user
        )

        return qquser


class WEIBOAuthUserSerializer(serializers.Serializer):
    '''
       登录创建用户序列化器
       用于绑定openid和账户
       1.openid
       2.手机号
       3.密码
       4.手机验证码
       '''
    access_token = serializers.CharField(label='操作凭证')
    mobile = serializers.RegexField(label='手机号', regex=r'^1[3-9]\d{9}$')
    password = serializers.CharField(label='密码', max_length=20, min_length=8)
    sms_code = serializers.CharField(label='短信验证码')

    def validate(self, attrs):
        access_token=attrs.get('access_token')
        if not access_token:
            raise serializers.ValidationError('error')
        attrs['access_token'] = access_token  # 用attrs传递数据

        # 验证mobile/sms_code
        mobile = attrs.get('mobile')
        sms_code = attrs.get('sms_code')
        redis_conn = get_redis_connection('code')
        redis_sms_code = redis_conn.get('sms_%s' % mobile)
        # 验证码校验
        if not redis_sms_code:
            raise serializers.ValidationError('验证码过期')

        # 最好删除短信
        redis_conn.delete('sms_' + mobile)
        if redis_sms_code.decode() != sms_code:
            raise serializers.ValidationError('验证码一致')

        # 3. 需要对手机号进行判断
        try:
            user = User.objects.get(mobile=mobile)
        except User.DoesNotExist:
        # 没有注册需要执行注册
            pass
        else:
            # 说明注册过,
            # 注册过需要验证密码
            if not user.check_password(attrs['password']):
                raise serializers.ValidationError('密码不正确')

            attrs['user'] = user

        return attrs

    def create(self,validate_data):
        user=validate_data.get('user')
        if user is None:
            user=User.objects.create(
                mobile=validate_data['mobile'],
                username=validate_data['username'],
                password=validate_data['password'],
            )
            user.set_password(validate_data['password'])
            user.save()
        wbuser=OAuthSinaUser.objects.create(
            user=user,
            access_token=validate_data['access_token']
        )
        return wbuser