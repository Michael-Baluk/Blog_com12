from django.urls import path
from .views import BlogInicio, PostDetalle, PostNuevo,PostEditar
from . import views




app_name = "blog"
urlpatterns = [
    path("", views.BlogInicio.as_view(),name= "blog_inicio"),
    path("Nuevo",views.PostNuevo.as_view(),name = "blog_nuevo"),
    path('editar/<str:slug>/', views.PostEditar.as_view(),name="blog_editar"),
    path('<str:slug>/', views.PostDetalle.as_view(),name="post_detalle"),
] 