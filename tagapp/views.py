from django.shortcuts import render
from tagapp.models import Tag
from conspectapp.models import Conspect


# Create your views here.
def tag_detail(request, tag_id):
    tag_detail_list = Tag.objects.get(id=tag_id).conspects
    tag_name = Tag.objects.get(id=tag_id).name
    return render(request, 'tagapp/tag_detail.html',{
        'tag_detail_list': tag_detail_list,
        'tag_name': tag_name,
    })

def str_all_tag():
	string_tag = ''
	conspects = Conspect.objects.all()
	for conspect in conspects:
		tags = conspect.tags.all()
		for tag in tags:
			string_tag += tag.name
			string_tag += ' '
	return string_tag


