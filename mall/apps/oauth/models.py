from django.db import models
from utils.models import BaseModel
# Create your models here.

#QQ登陆
class OAuthQQUser(BaseModel):
    user=models.ForeignKey('users.User',on_delete=models.CASCADE,verbose_name='用户')
    openid=models.CharField(max_length=64,verbose_name='openid',db_index=True)

    class Meta:
        db_table='tb_oauth_qq'
        verbose_name='QQ登陆用户'
        verbose_name_plural=verbose_name


#微博登陆
class OAuthSinaUser(BaseModel):
    """
    Sina登录用户数据
    """
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='用户')
    access_token = models.CharField(max_length=64, verbose_name='access_token', db_index=True)

    class Meta:
        db_table = 'tb_oauth_sina'
        verbose_name = 'sina登录用户数据'
        verbose_name_plural = verbose_name
