from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import permissions, viewsets

from .models import Book
from .serializers import BookSerializer
from .permissions import IsOwner


class BookViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    """API endpoint allowing books to be viewed or edited."""
    queryset = Book.objects.all().order_by("author", "title")
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    