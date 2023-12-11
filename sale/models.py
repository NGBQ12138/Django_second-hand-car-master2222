from django.db import models
from userinfo.models import UserInfo

# Create your models here.

FOR_CHOICES = (
    ('true', '是'),
    ('false', '否'),
)


FOR_EXAMINE = (
    ('1', '审核中'),
    ('2', '审核通过'),
    ('3', '审核不通过'),
)


class Brand(models.Model):
    logo_brand = models.ImageField(upload_to='img/logo', default='brandlogo.png', verbose_name='品牌logo')
    btitle = models.CharField(max_length=30, null=False, verbose_name='品牌')
    isDelete = models.BooleanField(default=False, verbose_name='是否删除')

    def __str__(self):
        return self.btitle


    class Meta:
        ordering = ["-id"]
        db_table = 'Brand'
        verbose_name = '车辆品牌表'
        verbose_name_plural = verbose_name


class Carinfo(models.Model):
    ctitle = models.CharField(max_length=30, null=False, verbose_name='车名')
    regist_date = models.DateField(default=False, verbose_name='上牌日期')
    engineNo = models.CharField(max_length=30, null=False, verbose_name='发动机号')
    mileage = models.IntegerField(default=10, verbose_name='公里数')
    maintenance_record = models.CharField(choices=FOR_CHOICES, default='false', max_length=10, verbose_name='维修记录')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='期望售价')
    extractprice = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='成交价格')
    newprice = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='新车价格')
    picture = models.ImageField(upload_to='img/car', default='normal.png', verbose_name='照片')
    formalities = models.CharField(choices=FOR_CHOICES, default='true', max_length=10, verbose_name='手续')
    debt = models.CharField(choices=FOR_CHOICES, default='false', max_length=10, verbose_name='债务')
    promise = models.TextField(null=True, verbose_name='卖家承诺')
    examine = models.CharField(max_length=30, choices=FOR_EXAMINE, default='1', verbose_name='审核进度')
    isPurchase = models.BooleanField(default=False, verbose_name='是否购买')
    serbran = models.ForeignKey(Brand, verbose_name='车辆型号', on_delete=models.CASCADE)
    user = models.ForeignKey(UserInfo, verbose_name='用户', on_delete=models.CASCADE)
    isDelete = models.BooleanField(default=False, verbose_name='是否删除')

    def __str__(self):
        return '{0}-{1}'.format(self.serbran, self.ctitle)

    def get_absolute_url(self):
        return '/sale/detail?carid={}'.format(self.id)


    class Meta:
        ordering = ["-id"]
        db_table = 'Carinfo'
        verbose_name = '车辆信息表'
        verbose_name_plural = verbose_name

