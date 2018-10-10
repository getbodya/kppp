from django.http import HttpResponseRedirect, HttpResponse
import cloudinary


def add_photo(request):
	if request.method == "POST":
		name = request.POST.get('name')
		file = request.FILES.get('img')
		response = cloudinary.uploader.upload(file, public_id=name, width=800, )
		print(response['url'])
		link = "![]({})".format(response['url'])
		print(link)
		return HttpResponse(link)
	return HttpResponse('OKhh')
