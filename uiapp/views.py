from django.shortcuts import render
from uiapp.models import Ui
from django.http import HttpResponse

# Create your views here.

def change_style(request):
    ui_style = request.GET['ui_style']
    ui_db = Ui.objects.all().filter(user_id=request.user.id).values('ui_title')[0]['ui_title']
    if ui_style != ui_db:
        Ui.objects.all().filter(user_id=request.user.id).values('ui_title').update(ui_title=ui_style)
        return HttpResponse("Cnbasdasd")

