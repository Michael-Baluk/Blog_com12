from django.forms import ModelForm
from django import forms
from .models import BlogPost, BlogComentario, BlogCategoria
from django.db.models            import Count


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


#class PostFilterForm(forms.Form):
  #  opciones= (('option 1', 'option1'),('option 2', 'option 2'),)
  #  def __init__(self, *args, **kwargs):
  #      super(PostFilterForm, self).__init__(*args, **kwargs)
  #      self.fields['comentarios']=forms.ChoiceField(choices=CHOICES)(
  #          queryset=  BlogPost.postobjects.annotate(comment_count=Count('comentarios')).filter(comment_count__gt=0).order_by('-comment_count'))
  #      self.fields['categoria']=forms.ModelChoiceField(
  #          queryset=BlogCategoria.objects.all())