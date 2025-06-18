from django import forms 
from django.contrib.auth.models import User


class ContactForm(forms.Form):
    name = forms.CharField(max_length=64)
    email = forms.EmailField()
    # Django's way of making a text area in HTML
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        """In practice, would implement actual email sending logic."""
        print(f"Sending email from {self.cleaned_data ['email']} with message: {self.cleaned_data ['message']}")
    

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ["username", "password", "password_confirm"]

    def clean(self):
        """Custom clean/validation function to ensure that certain
        conditions are met beyond Django built-in field validations.
        """
        # Cleans all data even after each field gets cleaned
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        # Make sure password and confirm exist and match
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match!")
        else:
            return cleaned_data
        