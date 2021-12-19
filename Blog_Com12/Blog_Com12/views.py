from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from apps.Usuarios.forms import CrearUsuarioForm

class Inicio(TemplateView):
    template_name = "inicio.html"
    

def register(request):
    form = CrearUsuarioForm()
    if request.method == 'POST':
        form = CrearUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_success')
    context= {'form': form}
    return render(request, "register.html", context)

def register_success(request):
    return render(request,'Usuarios/register_success.html',{})
