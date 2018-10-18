from django.shortcuts import render
from .models import Fask
from .forms import FaskForm

# Create your views here.
def form(request):
    if request.method == 'POST':
        form = FaskForm(request.POST)
        print(form)
        if form.is_valid():
            Fask(name=request.POST['name']).save()
    return render(request,'form_app/form.html')