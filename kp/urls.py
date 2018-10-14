from django.contrib import admin
from django.urls import path, include
from absapp import views
from conspectapp import views as conspect_views
from commentapp import views as comment_views
from ratingapp import views as rating_views
from tagapp import views as tag_views
from django.contrib.auth import views as auth_views
from uiapp import views as ui_views
from cloudapp import  views as cloud_views
from searchapp import  views as search_views
from likeapp import views as like_views
from askapp import views as ask_views
from django.conf.urls.i18n import i18n_patterns

urlpatterns =[
    path('admin/', admin.site.urls),
    path('', views.main, name='mainpage'),
    path('err/', views.err, name='error'),
    path('login/', auth_views.LoginView.as_view(template_name='absapp/login.html'), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('sign_up/', views.sign_up, name='sign-up'),

    path('userpage/<int:user_id>/', views.user_page, name='userpage'),
    path('userpage/edit/', views.user_edit, name='user_edit'),
    path('userpage/save_edit/', views.user_save_change, name='user_save_change'),
    path('userpage/create_conspect/', conspect_views.create_conspect,name='create_conspect'),
    path('user_reaction/',like_views.user_reaction, name='user_reaction'),
    path('userpage/new_create_conspect/', conspect_views.new_create_conspect,name='new_create_conspect'),
    path('userpage/make_conspect/',conspect_views.make_conspect,name='make_conspect'),

    path('conspect/<int:conspect_id>/', conspect_views.conspect, name='conspect'),
    path('conspect/<int:conspect_id>/edit/', conspect_views.conspect_edit, name='conspect_edit'),
    path('conspect/<int:conspect_id>/del/', conspect_views.conspect_del, name='conspect_del'),
    
    path('ask/<int:conspect_id>/', ask_views.ask_page, name='ask_page'),
    path('answer_page/<int:ask_id>/', ask_views.answer_page, name='answer_page'),
    path('check_new_message/',ask_views.check_new_message, name='check_new_message'), 
    path('q_and_a/', ask_views.q_and_a, name='q_and_a'),
    path('send_answer/', ask_views.response, name='response'),
    path('check_comment/', comment_views.check_comment, name='check_comment'),
    path('get_rating/', rating_views.get_rating, name='get_rating'),
    path('get_edit_conspect/', conspect_views.get_edit_conspect, name='get_edit_conspect'),
    path('tag/<int:tag_id>/', tag_views.tag_detail, name='tag_detail'),
    path('change_style/', ui_views.change_style, name='change_style'),
    path('add_photo/',cloud_views.add_photo, name='add_photo'),
    path('search/', search_views.search, name='search'),
    path('', include('social_django.urls')),
    path('i18n/', include('django.conf.urls.i18n')),

]