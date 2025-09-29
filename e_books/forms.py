from django import forms
from django.forms import widgets
from .models import Userregistration,Book
class User_registrationForm(forms.ModelForm):
    class Meta:
        model = Userregistration
        fields = '__all__'
        widgets = {
            "username": forms.TextInput(attrs={
                'placeholder': 'Enter username',
                'class': 'form-control'
            }),
            "email": forms.EmailInput(attrs={
                'placeholder': 'Enter email',
                'class': 'form-control'
            }),
            "password": forms.PasswordInput(attrs={
                'placeholder': 'Enter password',
                'class': 'form-control'
            }),
        }

class User_loginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter email',
            'class': 'form-control'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter password',
            'class': 'form-control'
        })
    )

      


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "published_date", "description"]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter book title"
            }),
            "author": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter author name"
            }),
            "published_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Enter book description",
                "rows": 4
            }),
         }