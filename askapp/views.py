from django.shortcuts import render
from askapp.models import Ask
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from conspectapp.models import Conspect
from django.template import loader
import datetime


def ask_page(request, conspect_id):
	conspect_author_id=Conspect.objects.get(id=conspect_id).author.id
	return render(request,'askapp/ask_page.html', {
		'conspect_author_id':conspect_author_id,
		})

def answer_page(request,ask_id):
	ask = Ask.objects.get(id=ask_id)
	Ask.objects.filter(id=ask_id).update(read=True)
	ask_story = []
	for item in Ask.objects.all().order_by('-created'):
		if item.who_ask == request.user and item.who_is_response == ask.who_ask or 	item.who_ask == ask.who_ask and item.who_is_response == request.user:
			ask_story.append(item)		
	return render(request,'askapp/answer_page.html',{
		'ask': ask.chat_text,
		'who_ask': ask.who_ask,
		'ask_id': ask_id,
		'ask_story': ask_story[0:20],
		})

def question(request):
    if request.method == "GET":
    	message = request.GET['message']
    	conspect_author_id = int(request.GET['conspect_author_id'])
    	responser = User.objects.get(id=conspect_author_id)
    	if responser == request.user:
    		return HttpResponse("сам у себя хочешь спросить?")
    	else:
    		Ask(who_ask=request.user, who_is_response=responser, chat_text=message).save()
    		return HttpResponse("Вопрос отправлен")

def response(request):
	if request.method == "GET":
		message = request.GET['message']
		ask_id = request.GET['ask_id']
		responser = Ask.objects.get(id=ask_id).who_ask
		Ask(who_ask=request.user, who_is_response=responser, chat_text=message).save()
		Ask.objects.filter(id=ask_id).update(answered=True)
		return HttpResponse("1")

def check_new_message(request):
	if request.method == "GET":
		last_ask = Ask.objects.filter(who_is_response=request.user.id).order_by('-created')[0]
		time_now = datetime.datetime.now()
		delta = time_now - last_ask.created
		print(last_ask.id)
		if delta.seconds < 5:
			return HttpResponse(last_ask.id)
		else:
			return HttpResponse(0)

