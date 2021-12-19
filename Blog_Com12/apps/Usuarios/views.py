from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from .models        import Usuario
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import PasswordChangeForm
from .forms import EditarUsuarioForm
from django.contrib.auth.views import PasswordChangeView
from django.urls                 import reverse_lazy

class UserPage(TemplateView):
    template_name = "Usuarios/usuario_info.html"
    model = Usuario
    context_object_name = 'usuario'
    def get_queryset(self):
        return Usuario.objects.all()
# Create your views here.

class EditarUsuario(generic.UpdateView):
    form_class = EditarUsuarioForm
    template_name = "Usuarios/usuario_edit.html"
    success_url = reverse_lazy('usuario:usuario_perfil')
    def get_object(self):
        return self.request.user


class EditarPassword(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name='Usuarios/usuario_password.html'
    success_url = reverse_lazy("usuario:password_success")
    
def password_success(request):
    return render(request,'Usuarios/password_success.html',{})