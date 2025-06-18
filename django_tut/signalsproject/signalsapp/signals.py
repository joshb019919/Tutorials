from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

from .models import User


@receiver(post_save, sender=User)
def log_create_user(sender, instance, **kwargs):
    print(f"user {instance} created at {datetime.now()}")
