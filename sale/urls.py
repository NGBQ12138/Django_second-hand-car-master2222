from django.urls import path, re_path, include
from django.contrib import admin
from sale import views

urlpatterns = [
    re_path(r'^$', views.protection, name='protection'),
    #详情页
    path(r'detail/', views.detail_one, name='buydetailone'),
    #以下是根据价格查询
    path(r'price0_10/', views.price0_10, name='price0_10'),
    path(r'price10_30/', views.price10_30, name='price10_30'),
    path(r'price30_80/', views.price30_80, name='price30_80'),
    path(r'price80_/', views.price80_, name='price80_'),

]