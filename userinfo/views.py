from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password, check_password
from django.db import DataError, DatabaseError
from django.http import request, response
from django.contrib import messages
from .models import *
from sale.models import *
import logging
import random
import json
# Create your views here.csrf_protect

auth_check = 'MarcelArhut'

#登入页面
def signin(request):
    return render(request, 'login.html')

#注册页面
def register(request):
    #检查用户是否已经通过身份验证
    if not request.user.is_authenticated:
        #进入注册页面
        return render(request, 'register.html')
    return redirect('/')
#我要卖车
def message(request):
    #检查用户是否已经通过身份验证
    if request.user.is_authenticated:
        #进入注册页面
        return render(request, 'message.html')
    return redirect('/')

def login_(request):
    if request.method == "POST":
        #从请求中获取名为“username”和“userpwd”的表单数据
        username = request.POST.get('username', '')
        password = request.POST.get('userpwd', '')
        #调用authenticate()方法对提供的凭据进行身份验证
        user = auth.authenticate(username=username, password=password)
        #判断user对象不为空且其状态为激活(is_active属性为True)，
        # 则使用Django的登录系统(auth.login())将用户登录到系统中。登录后，视图函数会重定向到根URL('/')以确保用户成功登录并返回主页
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('/')
        #user对象为空时，返回登入页面，并返回message值
        else:
            return render(request, 'login.html', {'message':"用户名或密码错误"})
    return HttpResponse(" ")


new_user = UserInfo()

#判断是买车还是卖车
def register_(request):
    if request.method == 'POST':
        # new_user = UserInfo()
        # try:
        #     #判断用户名是否存在
        #     olduser = UserInfo.objects.get(username=request.POST.get('username'))
        #     #如果用户名存在，则回到register.html页面，并返回message值
        #     return render(request, 'register.html', {'message': '用户名已经存在'})
        # except ObjectDoesNotExist:
        #     pass
        # if request.POST.get('userpwd') != request.POST.get('reuserpwd'):
        #     # 如果两次输入的密码不一致，则回到register.html页面，并返回message值
        #     return render(request, 'register.html', {'message': '两次输入的密码不一致'})
        # #用户密码的加密和添加
        # auth_check = None  # 根据具体情况定义auth_check变量
        # new_user.password = make_password(request.POST.get('userpwd'), auth_check, 'pbkdf2_sha1')
        #判断是否是进入买车页面
        if 'tobuy' in request.POST:
            # new_user.save()
            # {'new_user': new_user}
            return render(request, 'buyregister.html' )
        # 判断是否是进入卖车页面
        if 'tosale' in request.POST:
            # new_user.save()
            # {'new_user': new_user}
            return render(request, 'info-message.html')
    return render(request, 'register.html')


#买车信息添加
def buyinfo(request):
    if request.method == 'POST':
        new_user = UserInfo()
        new_user.username = request.POST.get("username")
        try:
            #判断用户名是否存在
            olduser = UserInfo.objects.get(username=new_user.username)
            #如果用户名存在，则回到register.html页面，并返回message值
            return render(request, 'buyregister.html', {'messname': '用户名已经存在'})
        except ObjectDoesNotExist:
            pass
        if request.POST.get('userpwd') != request.POST.get('reuserpwd'):
            # 如果两次输入的密码不一致，则回到register.html页面，并返回message值
            return render(request, 'buyregister.html', {'message': '两次输入的密码不一致'})
        #用户密码的加密和添加
        auth_check = None  # 根据具体情况定义auth_check变量
        new_user.password = make_password(request.POST.get('userpwd'), auth_check, 'pbkdf2_sha1')
        new_user.realname = request.POST.get("realname")
        new_user.uidentity = request.POST.get("identity")
        new_user.address = request.POST.get("address")
        new_user.cellphone = request.POST.get("phone")
        new_user.sex = request.POST.getlist("gender")[0]
        try:
            new_user.save()
        except ObjectDoesNotExist as e:
            logging.warning(e)
        return redirect('/')

#登出
def logout_(request):
    #注销当前已登录的用户并重定向到默认的登录页面
    auth.logout(request)
    return redirect('/')

#卖车页面
def infomes(request):
    return render(request, 'info-message.html')

#注册并卖车信息添加
def infomes_(request):
    # if request.is_ajax():
    if request.method == 'POST':
        # print(request.POST)
        #用户信息
        new_user = UserInfo()
        new_user.username = request.POST.get("username")
        try:
            # 判断用户名是否存在
            olduser = UserInfo.objects.get(username=new_user.username)
            # 如果用户名存在，则回到register.html页面，并返回message值
            return render(request, 'info-message.html', {'messname': '用户名已经存在'})
        except ObjectDoesNotExist:
            pass
        if request.POST.get('userpwd') != request.POST.get('reuserpwd'):
            # 如果两次输入的密码不一致，则回到register.html页面，并返回message值
            return render(request, 'info-message.html', {'message': '两次输入的密码不一致'})
        # 用户密码的加密和添加
        auth_check = None  # 根据具体情况定义auth_check变量
        new_user.password = make_password(request.POST.get('userpwd'), auth_check, 'pbkdf2_sha1')
        new_user.realname = request.POST.get("realname")
        new_user.uidentity = request.POST.get("identity")
        new_user.address = request.POST.get("address")
        new_user.cellphone = request.POST.get("phone")
        new_user.sex = request.POST.getlist("gender")[0]
        # 判断数据是否添加进数据库
        try:
            new_user.save()
        except ObjectDoesNotExist as e:
            logging.warning(e)
        #车辆
        brand = Brand()
        brand.btitle = request.POST.getlist("brands")[0]
        try:
            oldbrand = Brand.objects.filter(btitle=brand.btitle)
            if len(oldbrand) > 0:
                brand = oldbrand[0]
            else:
                brand.save()
        except DatabaseError as e:
            logging.warning(e)
        #卖车用户的车辆信息添加
        car = Carinfo()
        car.ctitle = request.POST.get("model")
        car.regist_date = request.POST.get("regist_date")
        car.engineNo = request.POST.get("engineNo")
        car.mileage = request.POST.get("mileage")
        car.maintenance_record = request.POST.getlist("isService")[0]
        car.price = request.POST.get("price")
        car.extractprice = int(car.price) * 0.02 + int(car.price)
        car.newprice = request.POST.get("newprice")
        car.picture = request.FILES.get('pic')
        car.formalities = request.POST.getlist("formalities")[0]
        car.debt = request.POST.getlist("isDebt")[0]
        car.promise = request.POST.get("promise")
        car.serbran = brand
        car.user = new_user
        #判断数据是否添加进数据库
        try:
            car.save()
        except ObjectDoesNotExist as e:
            #异常的详细信息
            logging.warning(e)
        return redirect("/")
    return HttpResponse(" ")

#我要卖车信息添加
def infomes_message(request):
    # if request.is_ajax():
    if request.user.is_authenticated:
        user_id = request.user.id
        # 车辆
        brand = Brand()
        brand.btitle = request.POST.getlist("brands")[0]
        try:
            oldbrand = Brand.objects.filter(btitle=brand.btitle)
            if len(oldbrand) > 0:
                brand = oldbrand[0]
            else:
                brand.save()
        except DatabaseError as e:
            logging.warning(e)
        #卖车用户的车辆信息添加
        car = Carinfo()
        car.ctitle = request.POST.get("model")
        car.regist_date = request.POST.get("regist_date")
        car.engineNo = request.POST.get("engineNo")
        car.mileage = request.POST.get("mileage")
        car.maintenance_record = request.POST.getlist("isService")[0]
        car.price = request.POST.get("price")
        car.extractprice = int(car.price) * 0.02 + int(car.price)
        car.newprice = request.POST.get("newprice")
        car.picture = request.FILES.get('pic')
        car.formalities = request.POST.getlist("formalities")[0]
        car.debt = request.POST.getlist("isDebt")[0]
        car.promise = request.POST.get("promise")
        car.serbran = brand
        car.user_id = user_id
        #判断数据是否添加进数据库
        try:
            car.save()
        except ObjectDoesNotExist as e:
            #异常的详细信息
            logging.warning(e)
        return redirect("/")
    return HttpResponse(" ")

#服务保障页面
def service(request):
    return render(request, 'service.html')




