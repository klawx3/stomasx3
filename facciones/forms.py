from django import forms

from .models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ["active","apikey","lastlogin"]

