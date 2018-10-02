from commentapp.models import Coment
from django import forms
from django.contrib.auth.models import User

from conspectapp.models import Conspect


class ComentForm(forms.ModelForm):
    content = forms.CharField(label='Комментарий')
    class Meta:
        model = Coment
        fields = ('content',)
