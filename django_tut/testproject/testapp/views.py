# django.contrib offers multiple built-ins to keep us from having to
# reinvent the wheel

# Allows session persistence for users
from django.contrib.auth import authenticate, login, logout
# Ensure that decorated views require login to access
from django.contrib.auth.decorators import login_required
# A class-based view to ensure that users are logged in
from django.contrib.auth.mixins import LoginRequiredMixin
# Built-in user model for validation for sessions
from django.contrib.auth.models import User, Group
from django.contrib.auth.views import LoginView
# A shortcut for HttpResponse(request, render(such-and-such))
from django.shortcuts import render
# A shortcut for render where URL name is used instead
from django.shortcuts import redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
# For RESTful views
from rest_framework import permissions, viewsets, generics
# A simple parent class for all class-based views
from django.views import View

from.serializers import GroupSerializer, UserSerializer, BookSerializer, ProfileSerializer
from .models import Product, Book, Profile
from .form import ContactForm
from .form import RegisterForm
from .permissions import IsOwner


# Create your views here.
def index_view(request):
    """Defines the home page, "index"."""
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "index.html", context)


def contact_view(request):
    """Defines the form page, "contact"."""
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect("contact-success")
    else:
        form = ContactForm()

    context = {"form": form}
    return render(request, "contact.html", context=context)


def contact_success_view(request):
    """Defines the successful form submission page, "success"."""
    return render(request, "contact-success.html")


def high_end_electronics(request):
    """Defines the page showing only expensive electronic products."""
    products = Product.objects.filter(value__gt=50.00, category=2)
    context = {"products": products}
    return render(request, "high-end-electronics.html", context)


def register_view(request):
    """Defines the page showing the register form."""
    if "POST" == str.upper(request.method):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = str(form.cleaned_data.get("username"))
            password = form.cleaned_data.get("password")
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect("books")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    """Use Django built-ins to add user to session."""
    if "POST" == str.upper(request.method):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get("next") or request.GET.get("next") or "books"
            return redirect(next_url)
        else:
            error_message = "Invalid credentials!"
    else: 
        error_message = ""
    
    return render(request, "accounts/login.html", {"error": error_message})


def logout_view(request):
    """Quick function to remove user from session."""
    if "POST" == str.upper(request.method):
        logout(request)
        return redirect("login")
    else:
        return redirect("home")


@login_required
def home_view(request):
    """Home view using login_required decorator."""
    return render(request, "auth1_app/home.html")


class ProtectedView(LoginRequiredMixin, View):
    """Protect the logged-in view for valid users."""
    login_url = "/login/"
    redirect_field_name = "redirect_to"

    def get(self, request):
        return render(request, "protected/protected.html")


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint allowing users to be viewed or edited.
    
    Groups views into viewsets rather than make multiple views.
    """
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
class GroupViewSet(viewsets.ModelViewSet):
    """API endpoint allowing groups to be viewed or edited.
    
    Groups views into viewsets rather than make multiple views.
    """
    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
def user_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
    else:
        redirect("login")
    

class BookViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    """API endpoint allowing books to be viewed or edited."""
    queryset = Book.objects.all().order_by("author", "title")
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    
    
class ProfileDetail(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
            
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        
    def perform_delete(self, instance):
        if instance.user != self.request.user:
            raise PermissionError("You don't have permission to view this profile.")
        instance.delete()
