from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from absapp.forms import  UserForm
from conspectapp.models import Conspect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from tagapp.views import str_all_tag
from uiapp.models import Ui

def main(request):
    ui = Ui.objects.get(user_id=request.user.id).ui_title
    tag_string = str_all_tag()
    toplist = Conspect.objects.order_by('-rating')[0:10]
    newlist = Conspect.objects.order_by('-created')[0:10]
    return render(request, 'absapp/main.html',{
        'tag_string':tag_string,
        'toplist': toplist,
        'newlist': newlist,
        'ui': ui,
    })


def err(request):
    return render(request, 'absapp/err.html',{})


def index(request):
    ui = Ui.objects.get(user_id=request.user.id).ui_title
    return render(request, 'absapp/index.html',{
        'ui': ui,
        })


@login_required(login_url = 'login')
def user_page(request, user_id):
    user_conspect_list = Conspect.objects.filter(author_id=user_id).all()
    return render(request, 'absapp/userpage.html',{
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
        field = request.GET['field']
        return HttpResponse('<form method="GET"><input type="text" id="edit_'+field+'"><button type="submit" onclick="replace(\''+field+'\')">submit</button></form>')


def user_save_change(request):
    if request.method == 'GET':
        new_val = request.GET['new_val']
        field = request.GET['field']
        print(new_val)
        User.objects.filter(username=request.user).update(field=new_val)
        return HttpResponse('ghbyzkasd')