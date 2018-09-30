from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from commentapp.forms import ComentForm
from commentapp.models import Coment
from conspectapp.models import Conspect
from conspectapp.forms import ConspectForm
from django.contrib.auth.decorators import login_required
import markdown2


# Create your views here.
@login_required(login_url = 'error')
def create_conspect(request):
    conspect_form = ConspectForm(request.POST)
    if request.method =='POST':
        if conspect_form.is_valid:
            conspect_form.save()
    return render(request, 'conspectapp/create_conspect.html',{
        'form':conspect_form,
    } )
def conspect_edit(request, conspect_id):
    conspect_name = Conspect.objects.filter(id=conspect_id).values('name')[0]['name']
    conspect_content = Conspect.objects.filter(id=conspect_id).values('content')[0]['content']
    return render(request, 'conspectapp/conspect_edit.html',{
        'conspect_name' : conspect_name,
        'conspect_content' : conspect_content,
        'conspect_id' :conspect_id,
    })

def get_edit_conspect(request):
    new_content = request.GET['content']
    new_conspect_name = request.GET['conspect_name']
    conspect_id = request.GET['conspect_id']
    Conspect.objects.filter(id=conspect_id).values('name').update(content=new_content)
    Conspect.objects.filter(id=conspect_id).values('name').update(name=new_conspect_name)
    return HttpResponse('Изменения сохранены')


def conspect(request,conspect_id):
    conspect_name = Conspect.objects.filter(id=conspect_id).values('name')[0]['name']
    conspect_content = Conspect.objects.filter(id=conspect_id).values('content')[0]['content']
    conspect_idd = Conspect.objects.filter(id=conspect_id).values('id')
    coment_list = Coment.objects.filter(conspect_id=conspect_id).order_by('-created')
    comment_form = ComentForm(request.POST)
    conspect_content2 = markdown2.markdown(conspect_content)
    if request.method =='POST':
        if comment_form.is_valid:
            comment_form.save()
            return HttpResponseRedirect(reverse('conspect',kwargs={
                'conspect_id' : conspect_id
            }))
    return render(request, 'conspectapp/conspect.html',{
        'conspect_id' : conspect_id,
        'coment_list' : coment_list,
        'comment_form' : comment_form,
        'conspect_name' : conspect_name,
        'conspect_content' : conspect_content2,
    })
