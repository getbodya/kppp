from django.shortcuts import render
from uiapp.models import Ui
from django.http import HttpResponse


def change_style(request):
    ui_style = request.GET['ui_style']
    print(ui_style)
    ui_db = Ui.objects.get(user_id=request.user.id).ui_title
    print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
    print(ui_style)
    print(ui_db)
    print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")

    if ui_style == "math":
    	Ui.objects.all().filter(user_id=request.user.id).values('ui_title').update(ui_title="gum")
    	return HttpResponse("gum")

    else:
        Ui.objects.all().filter(user_id=request.user.id).values('ui_title').update(ui_title="math")
        return HttpResponse("math")

