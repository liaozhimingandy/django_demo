import json

from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

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
    import random
    tmp_list = list()
    for _ in range(100):
        tmp_dict = dict()
        tmp_dict['a'] = 'a'
        tmp_dict['b'] = 'b'
        tmp_dict['c'] = random.randint(1,50)
        tmp_dict['d'] = 'd'
        tmp_dict['e'] = random.randint(1,50)
        tmp_list .append(tmp_dict)
    print(tmp_list)
    return HttpResponse(json.dumps({"data":tmp_list}))

