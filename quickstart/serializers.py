# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# ======================================================================
#   Copyright (C) 2020 liaozhimingandy@qq.com Ltd. All Rights Reserved.
#
#   @Author      : zhiming
#   @Project     : django_demo
#   @File Name   : serializers.py
#   @Created Date: 2020-11-01 21:49
#      @Software : PyCharm
#         @e-Mail: liaozhimingandy@qq.com
#   @Description : 序列化文件
#
# ======================================================================
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


def main():
    pass


if __name__ == "__main__":
    main()