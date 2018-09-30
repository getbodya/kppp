from django.shortcuts import render
from ratingapp.models import RatingModel
from django.http import HttpResponse, HttpResponseRedirect
from conspectapp.models import Conspect


def get_rating(request):
    user_vote = int(request.GET['rating'])
    conspect_id = int(request.GET['conspect_id'])
    
    sum_all_vote = Conspect.objects.filter(id=conspect_id).values('sum_all_vote')[0]['sum_all_vote']
    vote_counter = Conspect.objects.filter(id=conspect_id).values('vote_counter')[0]['vote_counter']
    sum_all_vote+=user_vote
    vote_counter+=1
    rating = round(sum_all_vote/vote_counter,2)
    Conspect.objects.filter(id=conspect_id).values('sum_all_vote').update(sum_all_vote=sum_all_vote)
    Conspect.objects.filter(id=conspect_id).values('vote_counter').update(vote_counter=vote_counter)
    Conspect.objects.filter(id=conspect_id).values('rating').update(rating=rating)

    if request.method =='GET':
        print(user_vote)
        return HttpResponse('<div>спасибо, твой голос для нас важен</div>')