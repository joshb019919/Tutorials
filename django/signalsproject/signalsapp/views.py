from django.shortcuts import render
from .models import User

# Create your views here.
def create_user_view(request):
    User.objects.create(name="Created User")
    return render(request, "blank.html")
