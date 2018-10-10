from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django.dispatch import receiver

# Create your models here.
class Ui(models.Model):
    ui_title = models.CharField(max_length=30, default='math')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Ui.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.ui.save()