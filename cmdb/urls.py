# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# ======================================================================
#   Copyright (C) 2020 liaozhimingandy@qq.com Ltd. All Rights Reserved.
#
#   @Author      : zhiming
#   @Project     : django_demo
#   @File Name   : urls.py
#   @Created Date: 2020-11-07 21:18
#      @Software : PyCharm
#         @e-Mail: liaozhimingandy@qq.com
#   @Description :
#
# ======================================================================

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
from django.contrib.auth import login
from django.urls import path
from django.conf.urls import url
from . import views

namespace = 'cmdb'

urlpatterns = [
    path(r'', views.overview, name='index'),
    path(r'base', views.base, name='base'),
    path(r'page', views.page, name='page'),
    # path(r'login', views.login, name='login')
    # url(r"^login/$", 'django.contrib.auth.views.login', {'template_name':'authorization/login.html'}, name ='login'),

]
