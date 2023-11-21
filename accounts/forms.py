from typing import Any
from django import forms
from accounts.models import User

class UserForm(forms.ModelForm):
    profile = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = ['email', 'full_name', 'profile', 'password']
        
        labels = {
            'email': 'Email',
            'full_name': 'Full Name',
            'profile': 'Profile',
            'password': 'Password',
        }
        
        help_texts = {
            'email': 'Enter your email address',
            'full_name': 'Enter your full name',
            'profile': 'Enter your profile image',
            'password': 'Enter your password',
        }