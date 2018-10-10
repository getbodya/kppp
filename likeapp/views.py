from django.shortcuts import render
from commentapp.models import Coment
from django.http import JsonResponse


def user_reaction(request):
	comment_id = request.GET.get('comment_id')
	comment = Coment.objects.get(id=comment_id)
	like = request.GET.get('like')
	dislike = request.GET.get('dislike')

	if like and (request.user not in comment.user_reaction.all()):
		comment.likes += 1
		comment.user_reaction.add(request.user)
		comment.save()
	"""
	if dislike and (request.user not in comment.user_reaction.all()):
		comment.dislikes += 1
		comment.user_reaction.add(request.user)
		comment.save()
		"""
	data = {
	 	"likes": comment.likes,
	 	#	"dislikes": comment.dislikes
	}
	return JsonResponse(data)