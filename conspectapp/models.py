from django.db import models
from django.contrib.auth.models import User
from tagapp.models import Tag

class Conspect(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField()
    specialty = models.CharField(max_length=100)
    rating = models.FloatField(default=0)
    sum_all_vote =models.PositiveIntegerField(default=0)
    vote_counter = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='conspects')

    def __str__(self):
        return self.name
