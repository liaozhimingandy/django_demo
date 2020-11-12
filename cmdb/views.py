import json

from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from .models import ServerAsset, DatabaseAsset
from django.contrib.auth.models import User

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
        item['fields']['updator'] = str(User.objects.get(id=item['fields']['updator']))
        item['fields']['creator'] = str(User.objects.get(id=item['fields']['creator']))
        tmp.append(item['fields'])  # 提取 'fields'字段的内容
    return HttpResponse(json.dumps({"data": tmp}))

@login_required(login_url="/admin/login/")
def list_database(request):
    return render(request, "cmdb/list_database.html")

@csrf_exempt
def data_database(request):
    tmp_data = serializers.serialize('json', DatabaseAsset.objects.all())
    result_json = json.loads(tmp_data)  # 对序列化之后的str类型数据进行转化为json对象
    tmp = list()
    for item in result_json:
        item['fields']['updator'] = str(User.objects.get(id=item['fields']['updator']))
        item['fields']['creator'] = str(User.objects.get(id=item['fields']['creator']))
        item['fields']['manage_ip'] = ServerAsset.objects.get(id=item['fields']['manage_ip']).manage_ip
        tmp.append(item['fields'])  # 提取 'fields'字段的内容

    return HttpResponse(json.dumps({"data": tmp*10000}))