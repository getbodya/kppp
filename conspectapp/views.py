from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from commentapp.forms import ComentForm
from commentapp.models import Coment
from conspectapp.models import Conspect
from tagapp.models import Tag
from conspectapp.forms import ConspectForm
from django.contrib.auth.decorators import login_required
import markdown2


# Create your views here.
@login_required(login_url = 'error')
def new_create_conspect(request):
    return render(request,'conspectapp/new_create_conspect.html',{})
    
@login_required(login_url = 'error')
def make_conspect(request):
    if request.method == "GET":
        Conspect(author=request.user,
            name=request.GET['name'],
            description=request.GET['description'],
            specialty=request.GET['specialty'],
            content=request.GET['content']
            ).save()
        tags = request.GET['tags']
        tag_list = tags.split(", ")
        all_tags = Tag.objects.all()
        all_tags_list = []
        for tag in Tag.objects.values('name'):
            all_tags_list.append(tag['name'])
        print(all_tags_list)
        for new_tag in tag_list:
            if new_tag not in all_tags_list:
                s = Tag(name=new_tag, count=1)
                s.save()
            elif new_tag in all_tags_list:
                s = Tag.objects.get(name=new_tag)
                s.count += 1
                s.save()
            conspect = Conspect.objects.filter(author=request.user).order_by('-created')[0]
            conspect.tags.add(s)
    return HttpResponse('Конспект сохранен')


def conspect_del(request,conspect_id):
    conspect = Conspect.objects.get(id=conspect_id)
    if request.user.id == conspect.author_id:
        conspect.delete()
        return redirect('/')
    else:
        return HttpResponse('')


def conspect_edit(request, conspect_id):
    conspect_name = Conspect.objects.get(id=conspect_id).name
    conspect_content = Conspect.objects.get(id=conspect_id).content
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
    conspect = Conspect.objects.filter(id=conspect_id).get()
    conspect_content = Conspect.objects.get(id=conspect_id).content
    coment_list = Coment.objects.filter(conspect_id=conspect_id).order_by('-created')
    comment_form = ComentForm(request.POST)
    conspect_content2 = markdown2.markdown(conspect_content)
    context = {
        'conspect_id': conspect_id,
        'coment_list': coment_list,
        'comment_form': comment_form,
        'conspect': conspect,
        'conspect_content': conspect_content2,
        }
    if request.method =='POST':
        if comment_form.is_valid:
            s=comment_form.save(commit=False)
            s.user = request.user
            s.conspect = conspect
            s.save()

            return render(request, 'conspectapp/conspect.html', context)
    return render(request, 'conspectapp/conspect.html',context)
