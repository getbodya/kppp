from django.db import models
from django.contrib.auth.models import User
from tagapp.models import Tag

class Conspect(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.FloatField(default=0)
    sum_all_vote =models.PositiveIntegerField(default=0)
    vote_counter = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='conspects')
    voted_user = models.ManyToManyField(User, blank=True, related_name='ratngs_conspects')

    def __str__(self):
        return self.name