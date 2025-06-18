from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Profile


class UserSerializer(serializers.ModelSerializer):
    """Turn user model data into JSON."""
    profile = serializers.PrimaryKeyRelatedField(many=True, queryset=Profile.objects.all())
    owner = serializers.ReadOnlyField(source="owner.username")
    
    class Meta:
        model = User
        fields = ["id", "username", "profile", "owner"]


class ProfileSerializer(serializers.ModelSerializer):
    """Turn profile model data into JSON."""
    class Meta:
        model = Profile
        fields = ["id", "title", "content", "author"]
        
    def create(self, validated_data):
        """Custom action to create a profile."""
        return Profile.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """Custom action to update a profile, setting the owner."""
        instance.title = validated_data.get("title", instance.title)
        instance.owner = validated_data.get("owner", instance.owner)
        instance.save()
        return instance
