"""trip URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    # 系统模块
    path('system/', include('system.urls')),
    # 景点相关的url
    path('sight/', include('sight.urls')),
    # 用户相关的url
    path('account/', include('accounts.urls')),
    # 订单模块
    path('order/', include('order.urls')),
    # 富文本
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # echarts
    path('master/', include('master.urls')),
    url(r'medias/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
]
