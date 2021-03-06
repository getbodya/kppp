from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Ask(models.Model):
    who_ask = models.ForeignKey(User, on_delete=models.CASCADE)
    who_is_response = models.ForeignKey(User, on_delete=models.CASCADE, related_name='responses')
    chat_text = models.TextField()
    read = models.BooleanField(default=False)
    answered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
