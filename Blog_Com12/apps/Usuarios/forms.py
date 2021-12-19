from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Usuario 


class CrearUsuarioForm(UserCreationForm):
    class Meta: 
        model = Usuario
        fields = ['username', 'email','password1', 'password2']

class EditarUsuarioForm(UserChangeForm):
    class Meta: 
        model = Usuario
        fields = ['first_name','last_name','resumen','imagen']
        exclude = ['username', 'email']
