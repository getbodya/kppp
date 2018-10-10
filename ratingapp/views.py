from django.http import HttpResponse
from conspectapp.models import Conspect

def get_rating(request):
    user_vote = int(request.GET['rating'])
    conspect_id = int(request.GET['conspect_id'])
    conspect =  Conspect.objects.get(id=conspect_id)

    if request.user not in conspect.voted_user.all():
        sum_all_vote = conspect.sum_all_vote
        vote_counter = conspect.vote_counter
        sum_all_vote+=user_vote
        vote_counter+=1
        rating = round(sum_all_vote/vote_counter,2)
        Conspect.objects.filter(id=conspect_id).values('sum_all_vote').update(sum_all_vote=sum_all_vote)
        Conspect.objects.filter(id=conspect_id).values('vote_counter').update(vote_counter=vote_counter)
        Conspect.objects.filter(id=conspect_id).values('rating').update(rating=rating)
        conspect.voted_user.add(request.user)

        return HttpResponse('<div>спасибо, твой голос для нас важен</div>')

    return HttpResponse('<div>ты уже голосовал</div>')

"""
def get_rating(request):
    user_vote = int(request.GET['rating'])
    conspect_id = int(request.GET['conspect_id'])

    if request.method =='GET':    
        sum_all_vote = Conspect.objects.get(id=conspect_id).sum_all_vote
        vote_counter = Conspect.objects.get(id=conspect_id).vote_counter
        sum_all_vote+=user_vote
        vote_counter+=1
        rating = round(sum_all_vote/vote_counter,2)
        Conspect.objects.filter(id=conspect_id).values('sum_all_vote').update(sum_all_vote=sum_all_vote)
        Conspect.objects.filter(id=conspect_id).values('vote_counter').update(vote_counter=vote_counter)
        Conspect.objects.filter(id=conspect_id).values('rating').update(rating=rating)
        
        return HttpResponse('<div>спасибо, твой голос для нас важен</div>')

        """