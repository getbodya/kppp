from django.db import models
from django.contrib.auth.models import User
from conspectapp.models import Conspect

# Create your models here.
class Coment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    conspect = models.ForeignKey(Conspect, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    user_reaction = models.ManyToManyField(User, blank=True, related_name='comments')
