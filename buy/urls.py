from django.urls import path, re_path, include
from django.contrib import admin
from buy import views

urlpatterns = [
    #买车详情
    path(r'addorder', views.add_order, name='addorder'),
    #买车
    path(r'buylist', views.buylist, name='buylist'),
    #个人中心
    path(r'userinfo', views.user_info, name='userinfo'),
    #确认购买
    path(r'confirmbuy', views.confirmbuy, name='confirmbuy'),
    #取消订单
    path(r'delcart', views.del_order, name='delcart'),
    #车辆品牌列表
    path(r'brandlist/', views.brandlist, name='brandlist'),
    #取消订单
    path(r'cancel_order/', views.cancel_order, name='cancelorder'),
    #个人信息
    path(r'alter_info/', views.alter_info, name='alter_info'),
    #卖车信息
    path(r'reoffer/', views.reoffer, name='reoffer'),
]

