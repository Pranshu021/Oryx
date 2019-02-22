from django.contrib.auth.models import User
from django import forms
from django.core import validators
from .models import UserInfo

def EmailValidator(emailed):
    if User.objects.filter(email=emailed).exists():
        raise forms.ValidationError("Email has already been Registered")


class UpdateProfileForm(forms.ModelForm):

    profile_pic = forms.ImageField(widget=forms.FileInput(attrs = {
        'class': 'profile-pic form-control btn btn-primary', 'placeholder': 'Upload a Profile Picture ...', 'accept': 'image/*'
    }), required=False)

    
    class Meta:
        model = UserInfo
        fields = ['profile_pic',]