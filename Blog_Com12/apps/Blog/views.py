from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .models import BlogPost
# Create your views here.
class BlogInicio(TemplateView):
    template_name = "Blog/blog_inicio.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = BlogPost.postobjects.all()
        return context

class PostDetalle(DetailView):
    model = BlogPost
    template_name = 'blog/post_detalle.html'
    context_object_name = 'post'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = BlogPost.objects.filter(slug=self.kwargs.get('slug'))
        return context
    
    
