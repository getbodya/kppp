from django.shortcuts import render
from tagapp.models import Tag


# Create your views here.
def tag_detail(request, tag_id):
    tag_detail_list = Tag.objects.get(id=tag_id).conspects
    return render(request, 'tagapp/tag_detail.html',{
        'tag_detail_list': tag_detail_list,
    })