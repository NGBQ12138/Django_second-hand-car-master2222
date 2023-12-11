from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserInfo)
# @admin.register(UserInfo)
# class UsersAdmin(admin.ModelAdmin):
    # list_display = ['username']
    # fields = ['username', 'password', 'realname']
    # actions_on_bottom = False
    # actions_on_bottom = True