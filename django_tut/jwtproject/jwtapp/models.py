from django.db import models


class Profile(models.Model):
    """Custom user profile model."""
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=64)
    content = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    owner = models.ForeignKey("auth.User", related_name="profile", on_delete=models.CASCADE)
        
    class Meta:
        ordering = ["created"]
