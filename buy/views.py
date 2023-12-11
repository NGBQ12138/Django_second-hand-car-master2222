from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from userinfo.models import *
from sale.models import Carinfo
from django.core.exceptions import ObjectDoesNotExist
from django.db import DatabaseError
from .models import *
from sale.models import *
import json
import datetime
import logging

# Create your views here.
#获取买车的信息
def add_order(request):  # 定义一个名为add_order的函数，接受一个request参数
    # 判断当前用户是否已经登录
    if request.user.is_authenticated:  # 如果用户已经登录
        # 获取查询字符串中名为 carid 的参数值
        car_id = request.GET.get('carid')  # 获取查询字符串中名为carid的参数值
        try:
            car_ = Carinfo.objects.get(id=car_id)  # 从数据库中获取指定ID的汽车信息
            brand = str(car_.serbran) + car_.ctitle  # 获取汽车品牌信息
            picture = car_.picture  # 获取汽车图片信息
            price = car_.extractprice  # 获取汽车成交价格信息
            newprice = car_.newprice  # 获取汽车新车价格信息
            mileage = car_.mileage  # 获取汽车公里数信息
            # 将用户信息和汽车信息保存到数据库中
            Cart.objects.create(suser=request.user, car=car_, brand=brand, picture=picture, price=price, newprice=newprice, mileage=mileage)  # 创建一个Cart对象，将用户信息和汽车信息保存到数据库中
        except ObjectDoesNotExist as e:  # 如果在获取汽车信息时出现异常（例如汽车不存在）
            logging.warning(e)  # 记录异常信息
        return render(request, 'order.html', {'car':locals()})  # 渲染并返回一个名为order.html的模板，并将局部变量作为上下文传递给模板
    else:  # 如果用户未登录
        return redirect('/user/login/')  # 重定向到登录页面


#确认购买
def confirmbuy(request):
    if request.user.is_authenticated:
        #请求中获取名为carid的参数值
        car_id = request.GET.get('carid')
        print(car_id)
        #生成一个当前时间的字符串
        orderNo = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        try:
            #根据carid查询购物车信息，并将查询结果保存到变量car_中
            car_ = Cart.objects.filter(car_id=car_id)
            car = Carinfo.objects.filter(id=car_id)
            # print(car[0].user)
            #从car_中获取品牌、图片、价格、优惠价、里程等信息，并保存到变量brand、picture、price、newprice、mileage中
            brand = car_[0].brand
            # print(brand)
            picture = car_[0].picture
            price = car_[0].price
            newprice = car_[0].newprice
            mileage = car_[0].mileage
            #使用Orders和Carinfo两个对象创建订单和更新数据库中的isPurchase字段为True
            Orders.objects.create(sale_user=car[0].user, buy_user=request.user, brand=brand, picture=picture, price=price, newprice=newprice, mileage=mileage, orderNo=orderNo)
            Carinfo.objects.filter(id=car_id).update(isPurchase='True')
            # car[0].isPurchase == 'True'
        except ObjectDoesNotExist as e:
            logging.warning(e)
        # 最近浏览
        try:
            #定义一个空列表rec_view_list,用于存储从数据库中查询出来的车辆信息
            rec_view_list = list()
            #get()从请求中的COOKIES中获取名为Recently_Viewed的值。如果该值不存在，则将其赋值为None
            if request.COOKIES.get('Recently_Viewed', None):
                #使用split()方法将rec_view字符串按照逗号分隔成一个字符串列表list_view
                rec_view = request.COOKIES.get('Recently_Viewed', None)
                list_view = rec_view.split(',')
                for i in list_view:
                    #使用Carinfo.objects.get()方法根据id字段查询数据库中对应的车辆信息，并将其添加到rec_view_list列表中
                    rec_view_list.append(Carinfo.objects.get(id=i))
            else:
                rec_view_list = []
        except ObjectDoesNotExist as e:
            logging.warning(e)

        user_id = request.user.id
        #查询最近4个被购买的车辆信息，并将查询结果保存到变量orders中
        orders = Orders.objects.filter(buy_user=user_id).order_by("-id")[:4]
        #查询当前用户信息，并将查询结果保存到变量user中
        user = UserInfo.objects.filter(id=user_id)[0]
        #查询当前用户未购买的4辆车辆信息，并将查询结果保存到变量car中
        car = Carinfo.objects.filter(user_id=user_id, isPurchase=False)[:4]
        return render(request, 'user-info.html', {'orders': locals()})
    else:
        return redirect('/user/login/')

# 取消订单
def del_order(request):
    # 获取用户ID
    user_id = request.user.id
    # 获取汽车ID
    car_id = request.GET.get('carid')
    try:
        # 尝试删除购物车中的订单
        Cart.objects.filter(suser_id=user_id, car_id=car_id).delete()
    except BaseException as e:
        # 记录异常信息
        logging.warning(e)
    # 重定向到主页
    return redirect('/')



# 买车列表
def buylist(request):
    # 从Carinfo数据表中取前8个车辆信息用于页面显示
    carlist = Carinfo.objects.filter(isPurchase=False, isDelete=False)
    # 检索了所有 Brand 对象的查询集，并按其 id 字段升序排序
    brandlist = Brand.objects.all().order_by('id')
    # 渲染 list.html 模板并返回结果
    paginator = Paginator(carlist, 8) # 每页显示8个
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'list.html', {'carlist':locals()})


# 个人中心
# 导入 get_object_or_404 函数
from django.shortcuts import get_object_or_404
def user_info(request):
    # 判断用户是否已登录
    if request.user.is_authenticated:
        # 初始化最近浏览过的车辆信息列表
        recently_viewed_cars = []
        try:
            # 定义一个空列表rec_view_list,用于存储从数据库中查询出来的车辆信息
            rec_view_list = list()
            # get()从请求中的COOKIES中获取名为Recently_Viewed的值。如果该值不存在，则将其赋值为None
            if request.COOKIES.get('Recently_Viewed', None):
                # 使用split()方法将rec_view字符串按照逗号分隔成一个字符串列表list_view
                rec_view = request.COOKIES.get('Recently_Viewed', None)
                list_view = rec_view.split(',')
                for i in list_view:
                    # 使用Carinfo.objects.get()方法根据id字段查询数据库中对应的车辆信息，并将其添加到rec_view_list列表中
                    rec_view_list.append(Carinfo.objects.get(id=i))
            else:
                rec_view_list = []
        except ObjectDoesNotExist as e:
            # 记录异常信息
            logging.error(e)

        # 使用request对象的user属性获取当前用户对象，并将用户id保存到变量user_id中
        user_id = request.user.id
        # 使用Orders对象的filter()方法根据buy_user字段筛选出所有属于当前用户的订单，并按id字段进行倒序排序(即从大到小排序),最后返回前4个数据
        orders = Orders.objects.filter(buy_user=user_id).order_by("-id")[:4]
        # 使用get_object_or_404()方法根据user_id查询数据库中对应用户信息，如果不存在则抛出Http404异常
        user_info = get_object_or_404(UserInfo, id=user_id)
        # 筛选出所有未被删除和未被购买的车辆信息，并按id字段进行倒序排序(即从大到小排序),最后返回前4个数据
        recent_cars = Carinfo.objects.filter(user_id=user_id, isDelete=False, isPurchase=False).order_by("-id")[:4]
        # 查询当前用户卖车信息信息
        car = Carinfo.objects.filter(user_id=user_id)

        # 渲染 user-info.html 模板并返回结果
        return render(request, 'user-info.html', {'orders': locals()})
    else:
        # 如果用户未登录，则重定向到登录页面
        return redirect('/user/login/')





# 取消订单
def cancel_order(request):
    # 获取用户ID
    user_id = request.user.id
    # 获取汽车ID
    car_id = request.GET.get('carid')
    try:
        # 更新数据库中对应的车辆信息，将isDelete字段设置为True
        Carinfo.objects.filter(user_id=user_id, id=car_id).update(isDelete=True)
    except ObjectDoesNotExist as e:
        # 记录异常信息
        logging.warning(e)
    # 重定向到用户信息页面
    return redirect('/buy/userinfo')



# 重新出价
def reoffer(request):
    #判断当前请求方法是否为POST
    #request.method == 'POST'
    if True:
        # 获取当前用户对象
        user_id = request.user.id
        # 获取POST请求中包含的carid参数值
        car_id = request.POST.get('carid')
        # 获取POST请求中包含的alterprice参数值（期望价格）
        alterprice = request.POST.get("alterprice")
        # 计算出修改后的价格并保存到变量extractprice中（成交价格）
        extractprice = int(alterprice) * 0.02 + int(alterprice)
        try:
            # 根据传入的参数更新数据库中指定车辆的信息
            Carinfo.objects.filter(user_id=user_id, id=car_id).update(price=alterprice, extractprice=extractprice)
        except ObjectDoesNotExist as e:
            # 记录异常信息
            logging.warning(e)
    # 重定向到用户信息页面
    return redirect('/buy/userinfo')



# 车辆品牌列表
def brandlist(request):
    # 获取GET请求中包含的brand参数值
    brand = request.GET.get('brand')
    try:
        # 根据传入的brand参数值查询数据库中对应的品牌信息
        brand = Brand.objects.get(btitle=brand)
        # 筛选出所有未被删除和未被购买的车辆信息
        carlist = brand.carinfo_set.filter(isPurchase=False, isDelete=False)
        # 检索了所有 Brand 对象的查询集，并按其 id 字段升序排序
        brandlist = Brand.objects.all().order_by('id')
    except ObjectDoesNotExist as e:
        # 记录异常信息
        logging.warning(e)
    # 渲染 list.html 模板并返回结果
    return render(request, 'list.html', {'carlist':locals()})



# 个人信息修改
def alter_info(requset):
    # 判断当前请求方法是否为POST
    if requset.method == 'POST':
        # 获取POST请求中包含的name参数值
        realname = requset.POST.get(key="name")
        # 获取POST请求中包含的sex参数值
        sex = str(requset.POST.get(key="sex"))
        print(sex)
        # 判断sex参数值并进行转换
        if sex == '男':
            sex = 1
        elif sex == '女':
            sex = 0
        # 获取POST请求中包含的phone参数值
        print(sex)
        phone = requset.POST["phone"]
        # 获取当前用户ID
        userid = requset.user.id
        # 根据传入的参数更新数据库中指定用户的信息
        UserInfo.objects.filter(id=userid).update(realname=realname, sex=sex, cellphone=phone)
        # 重定向到用户信息页面
        return redirect("/buy/userinfo")





