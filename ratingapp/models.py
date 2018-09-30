from django.db import models
from conspectapp.models import Conspect
from django.contrib.auth.models import User


class RatingModel(models.Model):
    conspect = models.ForeignKey(Conspect, on_delete=None)
    rating = models.FloatField()
    sum_all_vote =models.PositiveIntegerField()
    vote_counter = models.PositiveIntegerField()
    user = models.OneToOneField(User, on_delete=None)
