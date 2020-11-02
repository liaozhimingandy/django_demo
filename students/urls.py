# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# ======================================================================
#   Copyright (C) 2020 liaozhimingandy@qq.com Ltd. All Rights Reserved.
#
#   @Author      : zhiming
#   @Project     : django_demo
#   @File Name   : urls.py
#   @Created Date: 2020-11-01 22:19
#      @Software : PyCharm
#         @e-Mail: liaozhimingandy@qq.com
#   @Description : app下的urls配置
#
# ======================================================================

"""django_demo URL Configuration

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

from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from . import views

namespace = 'students'
# 路由列表
# urlpatterns = [
#     url(r'', views.StudentView.as_view(), name='students'),
# ]

urlpatterns = []
router = DefaultRouter()
router.register(r'', views.StudentViewSet) # 向路由器中注册视图集


urlpatterns += router.urls  # 将路由器中的所有路由信息追到到django的路由列表中

