from conspectapp.models import Conspect
from django import forms


class ConspectForm(forms.ModelForm):
	class Meta:
		model = Conspect
		fields = ('name', 'description', 'author','specialty', 'content', 'tags')
