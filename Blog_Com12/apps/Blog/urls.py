from django.urls import path
from django.conf.urls import url
from .views import BlogInicio, PostDetalle, PostNuevo, PostEditar, LikeView
from . import views




app_name = "blog"
urlpatterns = [
    path("", views.BlogInicio.as_view(),name= "blog_inicio"),
    path("Nuevo/",views.PostNuevo.as_view(),name = "blog_nuevo"),
    path('editar/<int:pk>/', views.PostEditar.as_view(),name="blog_editar"),
    path('<int:pk>/', views.PostDetalle.as_view(),name="post_detalle"),
    path('eliminar/<int:pk>/',views.PostEliminar.as_view(), name= "blog_eliminar"),
    path('comentario/<int:pk>/', views.ComentarioNuevo.as_view(),name="comentario_nuevo"),
    path('comentario/eliminar/<int:pk>/',views.ComentarioEliminar.as_view(), name= "comentario_eliminar"),
    path("like/<int:pk>/", LikeView, name="post_like")
] 