from django.forms import ModelForm
from django import forms
from .models import BlogPost, BlogComentario


class CrearPostForm(ModelForm):
    class Meta: 
        model = BlogPost
        fields = ['categoria','titulo','excerpt','contenido', 'imagen',]
    def __init__(self, *args, **kwargs):
        super(CrearPostForm, self).__init__(*args, **kwargs)
        for field in self: 
             field.field.widget.attrs['class'] = 'form-control'
        

class CrearComentarioForm(ModelForm):
    class Meta:
        model = BlogComentario
        fields = ['contenido',]