from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save,sender=User)
def login_user(sender, instance, created, **kwargs):
    if created:
        login(instance)