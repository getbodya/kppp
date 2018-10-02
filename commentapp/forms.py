from commentapp.models import Coment
from django import forms


class ComentForm(forms.ModelForm):
    content = forms.CharField(label='Комментарий')
    class Meta:
        model = Coment
        fields = ('content',)
