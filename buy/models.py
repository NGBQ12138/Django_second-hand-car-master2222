from django.db import models
from userinfo.models import UserInfo
from sale.models import Carinfo


# Create your models here.
ORDERSTATUS = (
        (1, "未出价",),  # 定义订单状态为未出价
        (2, "已出价"),  # 定义订单状态为已出价
        (3, "订单关闭"),  # 定义订单状态为订单关闭
    )


class Cart(models.Model):  # 定义购物车模型类
    suser = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name='买家')  # 定义买家字段，关联到UserInfo模型类
    car = models.ForeignKey(Carinfo, on_delete=models.CASCADE, verbose_name='车辆')  # 定义车辆字段，关联到Carinfo模型类
    brand = models.CharField(max_length=30, null=False, verbose_name='车辆信息')  # 定义车辆信息字段
    picture = models.ImageField(default='normal.png', verbose_name='照片')  # 定义照片字段
    price = models.CharField(max_length=30, null=False, verbose_name='成交价格')  # 定义成交价格字段
    newprice = models.CharField(max_length=30, null=False, verbose_name='新车价格')  # 定义新车价格字段
    mileage = models.CharField(max_length=30, null=False, verbose_name='公里数')  # 定义公里数字段

    def __str__(self):  # 定义__str__方法，返回品牌名称
        return self.brand

    class Meta:  # 定义Meta子类，用于设置模型类的选项
        db_table = 'Cart'  # 设置数据库表名称为Cart
        verbose_name='购物表'  # 设置模型在Django管理界面中显示的名称为购物表
        verbose_name_plural = verbose_name  # 设置模型复数形式的名称


class Orders(models.Model):  # 定义订单模型类
    sale_user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='suser', verbose_name='卖家')  # 定义卖家字段，关联到UserInfo模型类
    buy_user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='buser', verbose_name='买家')  # 定义买家字段，关联到UserInfo模型类
    brand = models.CharField(max_length=30, null=False, verbose_name='车辆信息')  # 定义车辆信息字段
    picture = models.ImageField(default='normal.png', verbose_name='照片')  # 定义照片字段
    price = models.CharField(max_length=30, null=False, verbose_name='成交价格')  # 定义成交价格字段
    newprice = models.CharField(max_length=30, null=False, verbose_name='新车价格')  # 定义新车价格字段
    mileage = models.CharField(max_length=30, null=False, verbose_name='公里数')  # 定义公里数字段
    orderNo = models.CharField(max_length=30, null=False, verbose_name='订单号')  # 定义订单号字段
    orderStatus = models.IntegerField(blank=True, choices=ORDERSTATUS,default='1',verbose_name='订单状态')#定义订单状态字段，使用ORDERSTATUS元组作为选项
    isDelete = models.BooleanField(default=False, verbose_name='是否删除')#定义是否删除字段

    def __str__(self):#定义__str__方法，返回品牌名称
        return self.brand

    def get_orderStatusDisplay(self):#定义get_orderStatusDisplay方法，根据订单状态返回相应的文本描述
        if self.orderStatus == 1:
            return u'未出价'
        elif self.orderStatus == 2:
            return u'已出价'
        elif self.orderStatus == 3:
            return u'订单关闭'
        else:
            return u''

    class Meta:#定义Meta子类，用于设置模型类的选项
        db_table = 'Orders'#设置数据库表名称为Orders
        verbose_name = '订单表'#设置模型在Django管理界面中显示的名称为订单表
        verbose_name_plural = verbose_name#设置模型复数形式的名称
