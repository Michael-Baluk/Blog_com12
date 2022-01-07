from django.forms import ModelForm
from django import forms
from .models import BlogPost, BlogComentario, BlogCategoria
from django.db.models            import Count
from bootstrap_modal_forms.forms import BSModalModelForm


class CrearPostForm(ModelForm):
    class Meta: 
        model = BlogPost
        fields = ['categoria','titulo','excerpt','contenido', 'imagen',]
    def __init__(self, *args, **kwargs):
        super(CrearPostForm, self).__init__(*args, **kwargs)
        for field in self: 
             field.field.widget.attrs['class'] = 'form-control'
        

class CrearComentarioForm(BSModalModelForm):
    class Meta:
        model = BlogComentario
        fields = ['contenido',]
    def __init__(self, *args, **kwargs):
        super(CrearComentarioForm, self).__init__(*args, **kwargs)
        for field in self: 
             field.field.widget.attrs['class'] = 'form-control'

class PostFilterForm(forms.Form):
    #comentarios = forms.ModelChoiceField(BlogPost.postobjects.annotate(comment_count=Count('comentarios')).filter(comment_count__gt=0), required=False)
    titulo = forms.CharField(required=False)
    categoria = forms.ModelChoiceField(required=False, queryset=BlogCategoria.objects.all())
    def __init__(self, *args, **kwargs):
        super(PostFilterForm, self).__init__(*args, **kwargs)
