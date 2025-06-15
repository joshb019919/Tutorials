from django.contrib.auth.models import User, Group
from django.db.models.functions import Now
from rest_framework import serializers
from decimal import Decimal
from datetime import datetime

from .models import Book, LANGUAGE_CHOICES, STYLE_CHOICES


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Validate User model input from user."""
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]
        

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """Validate Group model input from user."""
    class Meta:
        model = Group
        fields = ["url", "name"]
        
        
def validate_publish_date(published_date):
    """Validate that publish date is not in the future."""
    if published_date > datetime.now().date():
        raise serializers.ValidationError("Book must have been published in the past.")   
        
        
class BookSerializer(serializers.HyperlinkedModelSerializer):
    """Validate Book model input from user."""
    published_date = serializers.DateField(validators=[validate_publish_date])
    price = serializers.DecimalField(max_digits=6, decimal_places=2, min_value=Decimal("0.01"))
    
    class Meta:
        model = Book
        fields = ["title", "author", "published_date", "price"]
