from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User


class EmailAuthenticationForm(AuthenticationForm):

    def clean_username(self):
        return self.cleaned_data['username']

    class Meta:
        model = User
        fields = ['email', 'password']
