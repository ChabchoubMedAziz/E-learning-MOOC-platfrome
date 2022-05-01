from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control",


            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):

    gen = [
        ('m','Male'),
        ('f','Female'),
    ]

    ctry = [
        ('Australia','Australia'),
        ('Bangladesh','Bangladesh'),
        ('Brazil','Brazil'),
        ('Canada','Canada'),
        ('China','China'),
        ('France','France'),
        ('Germany','Germany'),
        ('India','India'),
        ('Italy','Italy'),
        ('Mexico','Mexico'),
        ('Pakistan','Pakistan'),
        ('Spain','Spain'),
        ('Tunisia','Tunisia'),
        ('United Kingdom','United Kingdom'),
        ('United States','United States'),
        ('Other','Other'),
    ]

    stt = [
        ("Bachelor's","Bachelor's"),
        ("Doctorate","Doctorate"),
        ("Master's","Master's"),
        ("Secondary","Secondary"),
    ]

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    YoB = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "class": "form-control"
            },
        format='%Y-%m-%d',     
        )
    )


    gender = forms.ChoiceField(
        
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        ),
        required=True,
        error_messages={'required':'Please entre your gender info', 'invalid_choice':'please select a valid choice'},
        choices=gen,

    )
    
    country = forms.ChoiceField(
        
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        ),
        required=True,
        error_messages={'required':'Please entre your country info', 'invalid_choice':'please select a valid choice'},
        choices=ctry,

    )

    state = forms.ChoiceField(
        
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        ),
        required=True,
        error_messages={'required':'Please entre your state info', 'invalid_choice':'please select a valid choice'},
        choices=stt,

    )



    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'YoB','gender' , 'country', 'state', 'is_teacher', 'is_student')
