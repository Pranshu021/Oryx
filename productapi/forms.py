from django import forms
from .models import Smartphone, Rated


class AboutTheProductForm(forms.ModelForm):
    about = forms.CharField(required=True, max_length=500, widget=(forms.Textarea(attrs={
        'class': 'form-control text-area', 'placeholder': 'Write Anything about the Product ....', 'cols': '30', 'rows': '5',
    })))


    class Meta:
        model = Rated
        fields = ['about']