from django.contrib import admin
from django.contrib.auth import views as views_auth
from django.urls import path
from . import views
from .views import UserPage, EditarUsuario, EditarPassword

app_name = "usuario"
urlpatterns = [
    path("register/",views.register, name = 'register'),
    path('login/', views_auth.LoginView.as_view(template_name="login.html"), name = 'login'),
    path('logout/', views_auth.logout_then_login, name = 'logout'),
    path("register_success/",views.register_success,name="register_success"),
    path("perfil/",views.UserPage.as_view(),name="usuario_perfil"),
    path("perfil/editar",views.EditarUsuario.as_view(),name="usuario_editar"),
    path("password/",views.EditarPassword.as_view(),name="usuario_password"),
    path("password_success/",views.password_success,name="password_success"),
    path("contacto", views.contact_view, name = "contacto")
 

]

