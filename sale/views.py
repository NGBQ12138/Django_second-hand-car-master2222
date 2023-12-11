from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
import logging
from .models import *
from userinfo.models import *
import random

# Create your views here.


def protection(request):
    #跳转协议内容界面
    return render(request, 'protection.html')


# 首页展示
from django.core.paginator import Paginator

def index(request):
    # 获取GET请求中包含的brand参数值
    brand = request.GET.get('brand')
    # 判断brand参数值是否为None
    if not brand:
        try:
            # 使用Carinfo对象的filter()方法根据isPurchase=False和isDelete=False条件筛选出所有未被购买和未被删除的车辆信息，并返回一个查询结果
            car_list = Carinfo.objects.filter(isPurchase=False, isDelete=False)
            # 将信息按id字段进行排序后保存到变量brandlist中
            brandlist = Brand.objects.all().order_by('id')
        except ObjectDoesNotExist as e:
            # 记录异常信息
            logging.warning(e)
    else:
        # 根据brand参数值从数据库中查询对应的品牌信息，并将查询结果保存到变量brand中
        brand = Brand.objects.get(btitle=brand).all()
    # 渲染 index.html 模板并返回结果
    return render(request, 'index.html', {'carlist':locals()})




# 详情页
def detail_one(request):
    # 获取GET请求中包含的carid参数值
    car_id = request.GET.get("carid")
    try:
        # 根据传入的carid参数值查询数据库中对应的车辆信息
        carone = Carinfo.objects.filter(id=car_id)
    except ObjectDoesNotExist as e:
        # 记录异常信息
        logging.warning(e)

    # 判断浏览器中是否存在名为Recently_Viewed的cookie
    if request.COOKIES.get('Recently_Viewed'):
        # 获取浏览器中保存的最近访问过的车辆信息
        cookie_car = request.COOKIES.get('Recently_Viewed')
        # 将cookie_car字符串按照逗号分隔符进行分割
        list_car = cookie_car.split(',')
        # 判断当前车辆ID是否已存在于list_car列表中
        if car_id in list_car:
            # 如果存在，则将其从列表中移除
            list_car.remove(car_id)
        # 判断list_car列表的长度是否大于等于2
        if len(list_car) >= 2:
            # 如果是，则将列表中最后一个元素弹出
            list_car.pop()
        # 将当前车辆ID添加到list_car列表的开头位置
        list_car = [car_id] + list_car
        # 将list_car列表转换为字符串并保存到变量cookie_car_new中
        cookie_car_new = ','.join(list_car)
    else:
        # 如果浏览器中不存在名为Recently_Viewed的cookie，则直接将当前车辆ID赋值给变量cookie_car_new
        cookie_car_new = car_id

    # 渲染 detail.html 模板并返回结果
    response = render(request, 'detail.html', {'carone':carone[0]})
    # 在响应对象中设置名为Recently_Viewed的cookie，其值为cookie_car_new，有效期为3000秒
    response.set_cookie('Recently_Viewed', cookie_car_new, max_age=3000)
    return response



#价格区间0-10
def price0_10(request):
    # 查询字符串中名为 brand 的参数值
    brand = request.GET.get("brand")
    # 获取所有品牌信息，并按品牌名称(即对象的 btitle 属性)排序
    brandlist = Brand.objects.all().order_by('id')
    # 判断brand参数值是否为'None'
    if not brand:
        try:
            # 使用默认的过滤条件从数据库中检索未购买和未删除的汽车信息，并将检索到的品牌信息重新按 ID 排序后返回
            carlist = Carinfo.objects.filter(isPurchase=False, isDelete=False, extractprice__lt=10, extractprice__gt=0)
            brandlist = Brand.objects.all().order_by('id')
        except ObjectDoesNotExist as e:
            # 记录异常信息
            logging.warning(e)
    else:
        try:
            # 根据查询字符串中名为 brand 的参数值从数据库中检索对应的品牌信息，并获取品牌ID
            brand_id = Brand.objects.filter(btitle=brand)[0].id
            # 根据传入的brand_id参数值和其他过滤条件从数据库中检索对应的车辆信息
            carlist = Carinfo.objects.filter(serbran_id=brand_id, isPurchase=False, isDelete=False, extractprice__lt=10, extractprice__gt=0)
        except ObjectDoesNotExist as e:
            # 记录异常信息
            logging.warning(e)
    # 渲染 list.html 模板并返回结果
    return render(request, 'list.html', {'carlist':locals()})



def price10_30(request):
    brand = request.GET.get("brand")
    brandlist = Brand.objects.all().order_by('id')
    if not brand:
        try:
            carlist = Carinfo.objects.filter(isPurchase=False, isDelete=False, extractprice__lt=30, extractprice__gt=10)
            brandlist = Brand.objects.all().order_by('id')
        except ObjectDoesNotExist as e:
            logging.warning(e)
    else:
        try:
            brand_id = Brand.objects.filter(btitle=brand)[0].id
            carlist = Carinfo.objects.filter(serbran_id=brand_id, isPurchase=False, isDelete=False, extractprice__lt=30,extractprice__gt=10)
        except ObjectDoesNotExist as e:
            logging.warning(e)
    return render(request, 'list.html', {'carlist1':locals()})


def price30_80(request):
    brand = request.GET.get("brand")
    brandlist = Brand.objects.all().order_by('id')
    if not brand:
        try:
            carlist = Carinfo.objects.filter(isPurchase=False, isDelete=False, extractprice__lt=80, extractprice__gt=30)
            brandlist = Brand.objects.all().order_by('id')
        except ObjectDoesNotExist as e:
            logging.warning(e)
    else:
        try:
            brand_id = Brand.objects.filter(btitle=brand)[0].id
            carlist = Carinfo.objects.filter(serbran_id=brand_id, isPurchase=False, isDelete=False, extractprice__lt=80,
                                             extractprice__gt=30)
        except ObjectDoesNotExist as e:
            logging.warning(e)
    return render(request, 'list.html', {'carlist': locals()})


def price80_(request):
    brand = request.GET.get("brand")
    brandlist = Brand.objects.all().order_by('id')
    if not brand:
        try:
            carlist = Carinfo.objects.filter(isPurchase=False, isDelete=False, extractprice__gt=80)
            brandlist = Brand.objects.all().order_by('id')
        except ObjectDoesNotExist as e:
            logging.warning(e)
    else:
        try:
            brand_id = Brand.objects.filter(btitle=brand)[0].id
            carlist = Carinfo.objects.filter(serbran_id=brand_id, isPurchase=False, isDelete=False, extractprice__gt=80)
        except ObjectDoesNotExist as e:
            logging.warning(e)
    return render(request, 'list.html', {'carlist': locals()})


