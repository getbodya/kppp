from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from absapp.forms import  UserForm
from conspectapp.models import Conspect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from tagapp.views import tag_dict
from uiapp.models import Ui
from askapp.models import Ask


def main(request):
    tag_dt = tag_dict()
    toplist = Conspect.objects.order_by('-rating')[0:10]
    newlist = Conspect.objects.order_by('-created')[0:10]
    return render(request, 'absapp/main.html',{
        'toplist': toplist,
        'newlist': newlist,
        'tag_dict':tag_dt,
    })


def err(request):
    return render(request, 'absapp/err.html',{})


def index(request):
    return render(request, 'absapp/index.html',{})


@login_required(login_url = 'login')
def user_page(request, user_id):
    user_conspect_list = Conspect.objects.filter(author_id=user_id).all()
    us = []
    last_ask = []
    user_answer_list = list(Ask.objects.filter(who_is_response=user_id).order_by('-created'))
    for item in user_answer_list:
        if item.who_ask not in us:
            us.append(item.who_ask)
    for item in us:
        s = Ask.objects.filter(who_ask=item).order_by('-created')[0]
        last_ask.append(s)
    


    user_ask_list = Ask.objects.filter(who_ask=user_id).order_by('-created')

    return render(request, 'absapp/userpage.html',{
        'last_ask':last_ask,
        'user_conspect_list' : user_conspect_list,
    })


def sign_up(request):
    user_form = UserForm()
    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_user.save()
            user = authenticate(
                username = user_form.cleaned_data['username'],
                password = user_form.cleaned_data['password']
            )
            login(request, user)

            return redirect(main)
    return render(request,'absapp/sign_up.html',{
        'user_form' : user_form,
    })


def logout_user(request):
    logout(request)
    return redirect(main)


def user_edit(request):
    if request.method == 'GET':
        return HttpResponse('<form method="GET"><input type="text" id="edit_'+field+'"><button type="submit" onclick="replace(\''+field+'\')">submit</button></form>')


def user_save_change(request):
    if request.method == 'GET':
        user = User.objects.get(username=request.user)
        user.username = request.GET['new_login']
        user.first_name = request.GET['new_first_name']
        user.last_name = request.GET['new_last_name']
        user.email = request.GET['new_email']
        user.save()
        return HttpResponse('Изменено')