from django.db import models

# Create your models here.
class Fask(models.Model):
    name = models.CharField(max_length=100, blank=False)