import json

from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from .models import ServerAsset

# Create your views here.
@login_required(login_url="/admin/login/")
def index(request):
    return render(request, "cmdb/dashboard.html")

# 此处借用admin的登录界面
@login_required(login_url="/admin/login/")
def base(request):
    if request.user.is_authenticated:
        print(request.user)
    return render(request, "cmdb/base.html")

@login_required(login_url="/admin/login/")
def overview(request):
    return render(request, "cmdb/overview.html")

@csrf_exempt
def page(request):
    tmp_data = serializers.serialize('json', ServerAsset.objects.all())
    result_json = json.loads(tmp_data)  # 对序列化之后的str类型数据进行转化为json对象
    tmp = list()
    for item in result_json:
        tmp.append(item['fields'])  # 提取 'fields'字段的内容
    return HttpResponse(json.dumps({"data": tmp}))

