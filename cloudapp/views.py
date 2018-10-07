from django.shortcuts import render ,redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import PhotoForm, UploadForm
import cloudinary

from cloudinary import utils

def add_photo(request):
	if request.method == "POST":
		x = request.POST.get('img')
		print('===================')
		print(x)
		print('===================')

		cloudinary.uploader.upload(x)
		#cloudinary.uploader.upload("./static/1.jpg")
		#utils.cloudinary_url(request.POST.get('img'),public_id = '1123')
		#cloudinary.utils.cloudinary_url(x)
		return HttpResponse('OK')
	return HttpResponse('OKhh')
