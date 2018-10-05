from django.shortcuts import render ,redirect
from .forms import PhotoForm, UploadForm
import cloudinary

def add_photo(request):
    #form = PhotoForm(request.POST, request.FILES)
    #s = cloudinary.CloudinaryImage("1.jpg").image()
    #image = request.FILES['image']
    #cloudinary.uploader.upload('./static/img/gum.jpg') загрузка с серва
    #cloudinary.uploader.upload(image)

    return render(request, 'cloudapp/add_photo.html', {
        #"form": form,
        #"s":s,
    })
