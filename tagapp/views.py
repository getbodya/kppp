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

def tag_dict():
    	tag_dct = {}
    	for tag in Tag.objects.all():
    		tag_dct[tag.name] = (tag.count, tag.id)
    	return tag_dct
