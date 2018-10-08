from django.http import HttpResponseRedirect, HttpResponse
import cloudinary


def add_photo(request):
	if request.method == "POST":
		name = request.POST.get('name')
		file = request.FILES.get('img')
		print('===================')
		print(file)
		print(name)
		print('===================')
		s = cloudinary.uploader.upload(file, public_id=name, width=800, )
		print(s['url'])
		link = "![]({})".format(s['url'])
		print(link)
		return HttpResponse(link)
	return HttpResponse('OKhh')
