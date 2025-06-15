from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Category(models.Model):
    name = models.CharField(max_length=127)


# Create your models here.
class Product(models.Model):
    # Django ORM handles everything!
    # Django will also automatically create the ID field
    name = models.CharField(max_length=64)
    value = models.DecimalField(blank=False, decimal_places=2, max_digits=5, default=Decimal())
    in_use = models.BooleanField(default=False)
    description = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)


    # String representation of products
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Price: {self.value}, Description: {self.description}"
    
    
class Book(models.Model):
    title = models.CharField(max_length=256, blank=False)
    author = models.CharField(max_length=64, blank=False)
    published_date = models.DateField(blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
