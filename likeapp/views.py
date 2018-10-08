from django.shortcuts import render
from commentapp.models import Coment
from django.http import JsonResponse
from django.views import View

# Create your views here.


class UserReactionView(View):

	template_name = 'conspectapp/conspect.html'

	def get(self, request, *args, **kwargs):
	 	comment_id = self.request.GET.get('comment_id')
	 	comment = Coment.objects.get(id=comment_id)
	 	like = self.request.GET.get('like')
	 	dislike = self.request.GET.get('dislike')
	 	print(comment_id)
	 	print(comment)
	 	print(like)
	 	print(dislike)

	 	return  HttpResponse('ok')


def user_reaction(request):
	comment_id = request.GET.get('comment_id')
	comment = Coment.objects.get(id=comment_id)
	like = request.GET.get('like')
	dislike = request.GET.get('dislike')

	if like and (request.user not in comment.user_reaction.all()):
		comment.likes += 1
		comment.user_reaction.add(request.user)
		comment.save()
	
	if dislike and (request.user not in comment.user_reaction.all()):
		comment.dislikes += 1
		comment.user_reaction.add(request.user)
		comment.save()
		
	data = {
	 	"likes": comment.likes,
	 	"dislikes": comment.dislikes
	}
	return JsonResponse(data)