from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Usuario 


class CrearUsuarioForm(UserCreationForm):
    class Meta: 
        model = Usuario
        fields = ['username', 'email','password1', 'password2']