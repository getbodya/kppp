from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ui(models.Model):
    ui_title = models.CharField(max_length=30, default='math')
    user = models.ForeignKey(User, on_delete=models.CASCADE)