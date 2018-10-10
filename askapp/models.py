from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Ask(models.Model):
    who_ask = models.OneToOneField(User, on_delete=models.CASCADE)
    who_is_response = models.OneToOneField(User, on_delete=models.CASCADE, related_name='responses')
    chat_text = models.TextField()
    def __str__(self):
        return self.who_ask +'>>>'+self.who_is_response

@receiver(post_save, sender=User)
def create_ask(sender, instance, created, **kwargs):
    if created:
        Ask.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_ask(sender, instance, **kwargs):
    instance.ui.save()