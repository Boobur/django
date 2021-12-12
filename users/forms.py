from django.forms import ModelForm, TextInput, PasswordInput, EmailInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms




class CreatUserForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center', 'placeholder':'Пароль'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center', 'placeholder':'Повторить пароль'}),
    )
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2'];
        widgets = {
            "username": TextInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Имя',
            }),
            
            "email": EmailInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Емайл', 
            }),
        }

        
