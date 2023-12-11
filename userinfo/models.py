from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
SEX_CHOICES = (
    ('0', '男'),
    ('1', '女'),
)

class UserInfo(AbstractUser):
    cellphone = models.CharField(max_length=11, null=False, verbose_name='手机')
    realname = models.CharField(max_length=50, null=False, verbose_name='姓名')
    uidentity = models.CharField(max_length=18, null=False, verbose_name='身份证')
    address = models.CharField(max_length=150, null=False, verbose_name='地址')
    sex = models.BooleanField(choices=SEX_CHOICES, default='0', max_length=10, verbose_name='性别')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'Users'
        verbose_name = '用户信息表'
        verbose_name_plural = verbose_name
