from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Usuario, Contactar


class CrearUsuarioForm(UserCreationForm):
    class Meta: 
        model = Usuario
        fields = ['username', 'email','password1', 'password2']
    def __init__(self, *args, **kwargs):
        super(CrearUsuarioForm, self).__init__(*args, **kwargs)
        for field in self: 
             field.field.widget.attrs['class'] = 'form-control'
    

class EditarUsuarioForm(UserChangeForm):
    class Meta: 
        model = Usuario
        fields = ['first_name','last_name','resumen','imagen']
        exclude = ['username', 'email']
        resumen=forms.CharField(max_length=250)

    def __init__(self, *args, **kwargs):
        super(EditarUsuarioForm, self).__init__(*args, **kwargs)
        for field in self: 
            field.field.widget.attrs['class'] = 'form-control'
             

class ContactForm(ModelForm):
    class Meta:
        model = Contactar
        fields = '__all__' 
        exclude = ('fecha','user')

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field in self: 
            field.field.widget.attrs['class'] = 'form-control'

    
