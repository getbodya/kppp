from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Conspect(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    description = models.TextField()
    content = models.TextField()
    specialty = models.CharField(max_length = 100)
    rating = models.FloatField(default = 0)
    sum_all_vote =models.PositiveIntegerField(default = 0)
    vote_counter = models.PositiveIntegerField(default = 0)
    
    def __str__(self):
        return self.name
