"""Blog_Com12 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as views_auth
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls,),
    path("", views.Inicio.as_view(), name= "inicio"),
    path('blog/', include('apps.Blog.urls', namespace='blog')),
    path('usuario/', include('apps.Usuarios.urls', namespace='usuario')),

    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='Usuarios/password_reset.html'),
     name= "reset_password"),

    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='Usuarios/password_reset_sent.html')
    , name= "password_reset_done"),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='Usuarios/password_reset_form.html'),
     name= "password_reset_confirm"),

    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='Usuarios/password_reset_done.html'),
     name= "password_reset_complete"),

]
urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
