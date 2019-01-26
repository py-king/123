#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:caozy time:19-1-6
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from rest_framework import serializers, status
from django_redis import get_redis_connection
from redis.exceptions import RedisError
import logging

from rest_framework.response import Response

from users.models import User

logger = logging.getLogger('memiduo')


class RegisterSMSCodeSerializer(serializers.Serializer):
    # 校验字段
    text = serializers.CharField(min_length=4, max_length=4, required=True, label='验证码')
    image_code_id = serializers.UUIDField(label='验证码唯一性id')

    # 对两个值进行判断
    def validate(self, attrs):
        text = attrs['text']
        image_code_id = attrs['image_code_id']
        redis_conn = get_redis_connection('code')
        redis_text = redis_conn.get('img_%s' % image_code_id)  # redis中获取验证码
        if not redis_text:  # 判断redis中是否获取到
            raise serializers.ValidationError('验证码过期')
        try:
            redis_conn.delete('img_%s' % image_code_id)  # 获取到将验证码记录删除
        except RedisError as e:
            logger.error(e)

        if redis_text.decode().lower() != text.lower():  # 比较redis中验证码和接收前端验证码
            raise serializers.ValidationError('验证码错误')
        return attrs



class AccountsRevSMSServializer(serializers.Serializer):
    '''验证手机验证码，返回信息'''

    user_name=serializers.CharField(label='用户名',max_length=20)
    sms_code = serializers.CharField(label='验证码校验', max_length=6, min_length=6, allow_null=False, allow_blank=False,
                                     write_only=True)

    def validate(self, attrs):
        user_name=attrs['user_name']
        try:
            user=User.objects.get(Q(username=user_name)|Q(mobile=user_name))
        except serializers.ValidationError:
            raise Exception('用户不存在')
        #在redis中获取sms
        sms_code=attrs.get('sms_code')
        mobile=user.mobile
        redis_conn=get_redis_connection('code')
        redis_sms_code=redis_conn.get('sms_%s'%mobile)
        if not redis_sms_code:
            raise serializers.ValidationError('验证码过期')
        if redis_sms_code.decode()!=sms_code:
            raise serializers.ValidationError('验证码一致')

        from .utils import generic_to_token
        token = generic_to_token(user.id)

        attrs['access_token']=token
        attrs['user_id']=user.id
        del attrs['sms_code']
        del attrs['user_name']
        # attrs={
        #     'access_token': token,
        #     'user_id': user.id
        # }
        print(attrs)
        return attrs

class ResetPasswordSerializer(serializers.Serializer):
    '''密码重置'''
    password = serializers.CharField(label='校验密码', allow_null=False, allow_blank=False, write_only=True)
    password2 = serializers.CharField(label='校验密码', allow_null=False, allow_blank=False, write_only=True)
    access_token=serializers.CharField(label='验证token')

    def validate(self, attrs):
        '''校验两次密码是否一直，手机验证码是否一致'''

        password1 = attrs.get('password')
        password2 = attrs.get('password2')
        if password1 != password2:
            raise serializers.ValidationError('两次输入的密码不一致')
        # token 验证
        access_token=attrs.get('access_token')
        from .utils import check_access_token
        user_id=check_access_token(access_token)
        attrs['user_id']=user_id
        try:
            user=User.objects.get(id=user_id)
        except serializers.ValidationError:
            raise Exception('token验证失败')
        # if user is None:
        #     return Response(status=status.HTTP_400_BAD_REQUEST)

        return attrs
    def update(self, instance, validated_data):

        password=validated_data['password']
        instance.password=password
        instance.set_password(password)
        instance.save()
        from utils.token_jwt import token_jwt
        token=token_jwt(instance)
        instance.access_token=token
        return instance

