from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Brand)
admin.site.register(Carinfo)



# @admin.register(Brand)
# class BrandAdmin(admin.ModelAdmin):
#     list_display = ['logo_brand', 'btitle']
#     list_display_link = ['logo_brand', 'btitle']
#     list_filter = ['logo_brand', 'btitle']
#     search_fields = ['logo_brand', 'btitle']
#     list_per_page = 10
#     fields = ['logo_brand', 'btitle', 'isDelete']
#     actions_on_top = False
#     actions_on_bottom = True
#
#
#
#
# @admin.register(Carinfo)
# class CarinfoAdmin(admin.ModelAdmin):
#     list_display = ['user', 'serbran', 'ctitle', 'price']
#     list_display_link = ['user', 'serbran', 'ctitle']
#     list_filter = ['user', 'serbran', 'ctitle']
#     search_fields = ['user', 'serbran', 'ctitle']
#     list_per_page = 10
#     fields = ['user', 'serbran', 'ctitle', 'regist_date',
#               'engineNo', 'mileage', 'maintenance_record', 'price','newprice', 'picture', 'formalities',
#               'debt', 'promise', 'examine']
#     actions_on_top = False
#     actions_on_bottom = True