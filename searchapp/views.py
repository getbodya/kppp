from django.shortcuts import render
from django.db.models import Q
from conspectapp.models import Conspect
from commentapp.models import Coment
# Create your views here.


def search(request):
    query = request.GET.get('q')
    founded = Conspect.objects.filter(
        Q(name__contains = query)|
        Q(content__contains = query))

    founded_comment = Coment.objects.filter(
        Q(content__contains=query))

    return render(request, 'searchapp/search.html',{
        'founded': founded,
        'founded_comment': founded_comment,

    })