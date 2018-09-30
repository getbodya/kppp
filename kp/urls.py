"""kp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from absapp import views
from conspectapp import views as conspect_views
from commentapp import views as comment_views
from ratingapp import views as rating_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('err/', views.err, name='error'),
    path('admin/', admin.site.urls),
    path('',views.main, name='mainpage'),
    path('login/', auth_views.LoginView.as_view(template_name='absapp/login.html'), name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('userpage/<int:user_id>/', views.user_page, name='userpage'),
    path('userpage/create_conspect/', conspect_views.create_conspect,name='create_conspect'),
    path('sign_up/', views.sign_up, name='sign-up'),
    path('conspect/<int:conspect_id>/', conspect_views.conspect, name='conspect'),
    path('conspect/<int:conspect_id>/edit/', conspect_views.conspect_edit, name='conspect_edit'),
    path('check_comment/', comment_views.check_comment, name='check_comment'),
    path('get_rating/', rating_views.get_rating, name='get_rating'),
    path('get_edit_conspect/', conspect_views.get_edit_conspect, name='get_edit_conspect'),
]
