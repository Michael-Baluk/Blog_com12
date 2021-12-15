from django.urls import path
from .views import BlogInicio, PostDetalle



app_name = "blog"
urlpatterns = [
    path("", BlogInicio.as_view(),name= "blog_inicio"),
    path('<slug:slug>/', PostDetalle.as_view(),name="post_detalle"),
] 
