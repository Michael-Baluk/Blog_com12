from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import UserPage, EditarUsuario, EditarPassword

app_name = "usuario"
urlpatterns = [
    path("perfil/",views.UserPage.as_view(),name="usuario_perfil"),
    path("perfil/editar",views.EditarUsuario.as_view(),name="usuario_editar"),
    path("password/",views.EditarPassword.as_view(),name="usuario_password"),
    path("password_success/",views.password_success,name="password_success"),
]

