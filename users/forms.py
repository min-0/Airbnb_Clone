from django.contrib.auth.models import User
from core import models
from django import forms
from . import models

class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data.get("eamil")
        try:
            models.User.objects.get(username=email)
        except models.User.DoesNotExist:
            raise forms.ValidationError("User does not exist")
            
    def clean_password(self):
        pass