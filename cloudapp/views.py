from django.shortcuts import render ,redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import PhotoForm, UploadForm
import cloudinary

from cloudinary import utils

def add_photo(request):
	if request.method == "POST":
		x = request.POST.get('sss')
		file = request.FILES.get('img')
		print('===================')
		print(x)
		print(file)
		print('===================')

		cloudinary.uploader.upload(file)
		
		return HttpResponse('OK')
	return HttpResponse('OKhh')
