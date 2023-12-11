from django.contrib import admin
from .models import *

admin.site.register(Cart)
admin.site.register(Orders)

# Register your models here.
# @admin.register(Orders)
# class OrdersAdmin(admin.ModelAdmin):
#     list_display = ['user', 'car', 'orderNo', 'orderStatus']
#     list_display_link = ['user', 'car', 'orderNo']
#     list_filter = ['user', 'orderNo']
#     search_fields = ['user', 'orderNo']
#     list_per_page = 10
#     fields = ['user','car', 'orderNo', 'orderStatus', 'cals', 'picture']
#     actions_on_top = False
#     actions_on_bottom = True