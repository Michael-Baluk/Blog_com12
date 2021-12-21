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
from django.contrib.auth import views as views_auth
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls,),
    path("register/",views.register, name = 'register'),
    path('login/', views_auth.LoginView.as_view(template_name="login.html"), name = 'login'),
    path('logout/', views_auth.logout_then_login, name = 'logout'),
    path("", views.Inicio.as_view(), name= "inicio"),
    path('blog/', include('apps.Blog.urls', namespace='blog')),
    path('usuario/', include('apps.Usuarios.urls', namespace='usuario')),
    path("register_success/",views.register_success,name="register_success"),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
