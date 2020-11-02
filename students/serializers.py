# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# ======================================================================
#   Copyright (C) 2020 liaozhimingandy@qq.com Ltd. All Rights Reserved.
#
#   @Author      : zhiming
#   @Project     : django_demo
#   @File Name   : serializers.py
#   @Created Date: 2020-11-02 20:11
#      @Software : PyCharm
#         @e-Mail: liaozhimingandy@qq.com
#   @Description : 序列化文件
#
# ======================================================================
from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    name = serializers.CharField(required=True, label='姓名')
    sex = serializers.BooleanField(required=True, label='性别')
    age = serializers.IntegerField(required=True, label='年龄')
    class_null = serializers.CharField(required=True, label='班级')
    description = serializers.CharField(label='描述')

    # 对数据进行验证
    def validate(self, attrs):
        tmp_age = attrs['age']
        if tmp_age < 18:
            raise serializers.ValidationError('年龄不允许<18')
        return super().validate(attrs)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.sex = validated_data.get('sex', instance.sex)
        instance.age = validated_data.get('age', instance.age)
        instance.class_null = validated_data.get('class_null', instance.class_null)
        instance.description = validated_data.get('description', instance.description)

        instance.save()
        return instance
    # class Meta:
    #     model = Student
    #     fields = ['id', 'name']



def main():
    pass


if __name__ == "__main__":
    main()