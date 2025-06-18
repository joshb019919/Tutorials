from rest_framework import serializers
from datetime import datetime
from decimal import Decimal
from .models import Book
        

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