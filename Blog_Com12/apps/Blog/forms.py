from django.forms import ModelForm
from django import forms
from .models import BlogPost, BlogComentario


class CrearPostForm(ModelForm):
    class Meta: 
        model = BlogPost
        fields = ['categoria','titulo','excerpt','contenido', 'imagen',]

class CrearComentarioForm(ModelForm):
    class Meta:
        model = BlogComentario
        fields = ['contenido',]