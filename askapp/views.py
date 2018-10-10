from django.shortcuts import render
from askapp.models import Ask
from django.http import HttpResponse

# Create your views here.
def ask_page(request, conspect_id):
    
    return render(request,'askapp/ask_page.html',{})

def q_and_a(re):
    if request.method == "GET":
        message = request.GET['messanges']
        print(message)
    return HttpResponse('ssss')