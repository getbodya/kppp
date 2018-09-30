from django.shortcuts import render
from commentapp.forms import ComentForm
from django.http import HttpResponse, HttpResponseRedirect
from commentapp.models import Coment
from django.template import loader
from django.urls import reverse


# Create your views here.
def check_comment(request):
    if request.method == "GET":
        s = request.GET['conspect_id']
        coment_list = Coment.objects.filter(conspect_id=s).order_by('-created')
        context = {
        'coment_list' : coment_list,
        } 
        template = loader.get_template("commentapp/comment.html")
        return HttpResponse(template.render(context))
