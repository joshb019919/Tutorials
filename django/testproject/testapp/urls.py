from django.urls import path, include
from . import views
from .form import ContactForm

# List of URL patterns available in app
urlpatterns = [
    # Paths to index, contact form, and form success pages
    # 
    # First field is path text after domain name:port
    # Second field is the view function to render
    # Third field is when the form is submitted correctly
    # 
    # Using the name kwarg allows redirect to simply use name rather
    # than giving it the request object, HTML page name, and optional
    # context 
    path("", views.index_view, name="index"),
    path("contact", views.contact_view, name="contact"),
    path("contact/success", views.contact_success_view, name="contact-success"),
    path("highend-electronics", views.high_end_electronics, name="highend-electronics"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    path("home/", views.home_view, name="home"),
    path("protected/", views.ProtectedView.as_view(), name="protected"),
]