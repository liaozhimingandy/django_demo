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
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'api_auth/', include('quickstart.urls')),
    path(r'api_auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'students/', include('students.urls')),
    path(r'cmdb/', include("cmdb.urls")),
    # url(r'accounts/login/$', 'django.contrib.auth.login'),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('change-password/', auth_views.PasswordChangeView.as_view()),
    # path('login/', auth_views.LoginView.as_view()),
]
