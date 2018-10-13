from django.shortcuts import render
from askapp.models import Ask
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from conspectapp.models import Conspect
import datetime


def ask_page(request, conspect_id):
	conspect_author_id=Conspect.objects.get(id=conspect_id).author.id
	return render(request,'askapp/ask_page.html', {
		'conspect_author_id':conspect_author_id,
		})

def answer_page(request,ask_id):
	ask = Ask.objects.get(id=ask_id)
	return render(request,'askapp/answer_page.html',{
		'ask': ask.chat_text,
		'who_ask': ask.who_ask,
		'ask_id': ask_id,
		})

def q_and_a(request):
    if request.method == "GET":
    	message = request.GET['message']
    	conspect_author_id = int(request.GET['conspect_author_id'])
    	responser = User.objects.get(id=conspect_author_id)
    	Ask(who_ask=request.user, who_is_response=responser, chat_text=message).save()
    	return HttpResponse("Вопрос отправлен")

def response(request):
	if request.method == "GET":
		message = request.GET['message']
		ask_id = request.GET['ask_id']
		responser = Ask.objects.get(id=ask_id).who_ask	
		print(message + "_____" + ask_id)
		Ask(who_ask=request.user, who_is_response=responser, chat_text=message).save()
		return HttpResponse("ответ отправлен")

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

