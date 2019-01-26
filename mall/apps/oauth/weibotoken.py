import requests
from urllib.parse import urlencode, parse_qs
import json

from mall import settings
from mall.settings import WEIBO_Key, WEIBO_REDIRECT_URI


# 微博使用post方法
def get_access_token(code):
    # 构建参数数据
    access_token_url = "https://api.weibo.com/oauth2/access_token"
    re_dict = requests.post(access_token_url, data={
        "client_id": settings.WEIBO_Key,
        "client_secret": settings.WEIBO_Secret,
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": settings.WEIBO_REDIRECT_URI,
    })

    # 提取数据   通过data=re_dict.text拿到token
    # '{"access_token":"2.00JPuQRBJcPibD06b259a62b9J4bJE","remind_in":"108873",
    # "expires_in":108873,"uid":"1171359995","isRealName":"true"}'
    try:
        data = re_dict.text

        data = eval(data)


    except:
        raise Exception('请求失败')

    # 提取access_token
    access_token = data.get('access_token', None)
    if not access_token:
        raise Exception('access_token获取失败')

    return access_token



# get方法，不适用
"""
def get_access_token(self, code):
    # 构建参数数据

    access_url = 'https://api.weibo.com/oauth2/authorize?'+'client_id='+WEIBO_Key+'&'+'redirect_uri='+WEIBO_REDIRECT_URI

    # 发送请求
    try:
        response = requests.get(access_url)

        # 提取数据
        # access_token=FE04************************CCE2&expires_in=7776000&refresh_token=88E4************************BE14
        data = response.text

        # 转化为字典
        data = parse_qs(data)
    except:
        raise Exception('请求失败')

    # 提取access_token
    access_token = data.get('access_token', None)

    if not access_token:
        raise Exception('access_token获取失败')

    return access_token[0]
"""
