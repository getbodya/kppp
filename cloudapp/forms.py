from django import forms
from .models import Photo



class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image', )

class UploadForm(forms.Form):
    image = forms.FileField()