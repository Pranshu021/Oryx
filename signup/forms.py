from django.contrib.auth.models import User
from django import forms
from django.core import validators

def Username_check(name):
    if User.objects.filter(username=name).exists():
        raise forms.ValidationError("Username Already Exists !")

def Email_check(emailed):
    if User.objects.filter(email=emailed).exists():
        raise forms.ValidationError("Email has Already been registered")

def Password_validator(password):
    if len(password) < 8:
        raise forms.ValidationError("Password must be atleast of 8 characters")

def ConvertToLowerCase(name):
        return name.lower()

class UserForm(forms.ModelForm):
    username = forms.CharField(required=True, max_length=50,widget=forms.TextInput(attrs={'class': 'textfield form-control','placeholder': 'Username'}),validators = [validators.MinLengthValidator(1), Username_check, ConvertToLowerCase])
    email = forms.EmailField(required=True, max_length=50,widget=forms.TextInput(attrs={'class': 'textfield form-control','placeholder': 'Email'}),validators = [validators.MinLengthValidator(1), Email_check])
    password = forms.CharField(required=True, max_length=50,widget=forms.PasswordInput(attrs={'class': 'textfield form-control','placeholder': 'Password'}),validators = [validators.MinLengthValidator(1), Password_validator,])
    confirm_password = forms.CharField(required=True, max_length=50,widget=forms.PasswordInput(attrs={'class': 'textfield form-control','placeholder': 'Re-type Password'}),validators = [validators.MinLengthValidator(1),])

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

