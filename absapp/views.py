from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from absapp.forms import  UserForm
from conspectapp.models import Conspect
from django.contrib.auth import authenticate, login, logout


def main(request):
    toplist = Conspect.objects.order_by('-rating')[0:10]
    newlist = Conspect.objects.order_by('-created')[0:10]
    return render(request, 'absapp/main.html',{
        'toplist': toplist,
        'newlist': newlist,
    })


def err(request):
    return render(request, 'absapp/err.html',{})


def index(request):
    return render(request, 'absapp/index.html',{})


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
