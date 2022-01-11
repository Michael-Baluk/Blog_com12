from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from apps.Usuarios.forms import CrearUsuarioForm

class Inicio(TemplateView):
    template_name = "inicio.html"
    

