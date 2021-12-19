from django.urls import path
from .views import BlogInicio, PostDetalle, PostNuevo,PostEditar
from . import views




app_name = "blog"
urlpatterns = [
    path("", views.BlogInicio.as_view(),name= "blog_inicio"),
    path("Nuevo/",views.PostNuevo.as_view(),name = "blog_nuevo"),
    path('editar/<int:pk>/', views.PostEditar.as_view(),name="blog_editar"),
    path('<int:pk>/', views.PostDetalle.as_view(),name="post_detalle"),
    path('eliminar/<int:pk>/',views.PostEliminar.as_view(), name= "blog_eliminar"),
    path('comentario/<int:pk>/', views.ComentarioNuevo.as_view(),name="comentario_nuevo"),
] 