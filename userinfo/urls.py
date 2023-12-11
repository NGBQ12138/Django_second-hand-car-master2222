from django.urls import path, re_path, include
from django.contrib import admin
from userinfo import views

urlpatterns = [
    #登入页面
    path(r'login/', views.signin, name='login'),
    #登入判断
    path(r'loginin/', views.login_, name='login_in'),
    #注册页面
    path(r'register/', views.register, name='register'),
    #注册判断
    path(r'registerin/', views.register_, name='register_in'),
    #注销
    path(r'logout/', views.logout_, name='logout'),
    #买车信息添加
    path(r'buyinfo/', views.buyinfo, name='buyinfo'),
    #进入卖车页面
    path(r'infomes/', views.infomes, name='infomes'),
    #卖车信息添加页面
    path(r'infomesin/', views.infomes_, name='infomes_in'),
    #服务保障页面
    path(r'service/', views.service, name='service'),
    #我要卖车
    path(r'message/', views.message, name='message'),
    #我要卖车信息添加
    path(r'infomes_message/', views.infomes_message, name='infomes_message'),
]