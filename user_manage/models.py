from django.db import models

# Create your models here.
# coding: utf-8
from django.db import models

# Create your models here.
# 用户注册
class User(models.Model):
    email = models.EmailField("邮箱")
    phone = models.IntegerField("手机号", default=0000000000)
    password = models.CharField("密码", max_length=255)
    account = models.DecimalField("账户余额", default=0, max_digits=8, decimal_places=2)

