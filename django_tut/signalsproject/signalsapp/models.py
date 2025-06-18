from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=64)
