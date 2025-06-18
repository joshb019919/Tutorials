from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=256, blank=False)
    author = models.CharField(max_length=64, blank=False)
    published_date = models.DateField(blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
