from django import forms
from .models import Fask

class FaskForm(forms.ModelForm):
    class Meta:
        model = Fask
        fields = ['name',]