#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:caozy time:19-1-10
from mall import settings



from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature


def generic_to_token(user):
    print(user)
    serializer = Serializer(settings.SECRET_KEY, expires_in=3600)
    data = {'user': user}
    token = serializer.dumps(data)
    return token.decode()


def check_access_token(access_token):
    print(access_token)
    serializer = Serializer(settings.SECRET_KEY, expires_in=3600)
    # 对数据进行loads操作
    try:
        data = serializer.loads(access_token)
    except BadSignature:
        return None
    return data['user']
