"""usedcar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, re_path, include
from django.contrib import admin
from django.views.generic import RedirectView

from sale import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'index', views.index, name='index'),
    re_path('^$', RedirectView.as_view(url='index/')),
    re_path(r'^user/', include('userinfo.urls')),
    re_path(r'^buy/', include('buy.urls')),
    re_path(r'^sale/', include('sale.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
