from . import forms, models
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import *
from django.urls import reverse
from django.template import loader
from django.views import generic


# Create your views here.
def index(request):
    return HttpResponse("hello world")


def login(request):
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('user_name')
            password = login_form.cleaned_data.get('user_password')

            try:
                user = models.JobHunter.objects.get(userName=username)
            except :
                message = '用户不存在！'
                return render(request, 'login/login.html', locals())

            if user.password == password:
                return redirect('/index/')
            else:
                message = '密码不正确！'
                return render(request, 'jmr/login.html', locals())
        else:
            return render(request, 'jmr/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'jmr/login.html', locals())



