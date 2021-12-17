from django.forms import ModelForm
from django import forms
from .models import BlogPost


class CrearPostForm(ModelForm):
    class Meta: 
        model = BlogPost
        fields = ['categoria','titulo','excerpt','contenido', 'imagen','autor',]