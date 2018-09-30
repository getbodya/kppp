from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput )
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
