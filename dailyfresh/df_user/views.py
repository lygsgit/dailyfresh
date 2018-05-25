from django.shortcuts import render, redirect
from .models import *
from hashlib import sha1
from django.http import HttpResponse, JsonResponse
import json

# Create your views here.
def register(request):
    return render(request, 'df_user/register.html')
def register_handle(request):
    # 接收用户数
    post = request.POST
    print(type(post))
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')
    # 判断两次密码
    if upwd != upwd2:
        return redirect('/user/register')
    # 密码加密
    s1 = sha1()
    s1.update(upwd.encode('utf8'))
    upwd3 = s1.hexdigest()

    # 创建对象
    user = UserInfo()
    user.uname = uname
    user.upwd =upwd3
    user.uemail = uemail
    user.save()
    # 注册成功，转到登陆页面
    return redirect('/user/login/')
def register_exist(request):
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname = uname).count()
    return JsonResponse({'count':count})
