from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.edit import UpdateView, DeleteView, FormView
from django.views.generic.detail import DetailView
from .models import BlogPost, BlogComentario
from .forms import CrearPostForm
# Create your views here.
class BlogInicio(ListView):
    template_name = "Blog/blog_inicio.html"
    model = BlogPost
    context_object_name = "posts"
    def get_queryset(self):
        return BlogPost.postobjects.all()
    
class PostDetalle(DetailView):
    model = BlogPost
    template_name = 'blog/post_detalle.html'
    context_object_name = 'post'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = BlogPost.objects.filter(slug=self.kwargs.get('slug'))
        return context

class PostComentario(DetailView):
    model = BlogComentario
    template_name= "blog/post_detalle.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comentarioss"] = BlogComentario.objects.all()
        return context
    
class PostNuevo(CreateView):
        template_name = 'Blog/blog_nuevo.html'
        model = BlogPost
        form_class = CrearPostForm
        
        def get_success_url(self, **kwargs):
         return reverse_lazy("blog:blog_inicio")

class PostEditar(UpdateView):
    template_name = 'blog/post_detalle.html'
    model = BlogPost
    form_class = CrearPostForm


    def get_success_url(self, **kwargs):
        return reverse_lazy('blog/post_detalle.html')

class AdminEliminar(DeleteView):
    template_name = 'blog/post_detalle.html'
    model = BlogPost
    success_url = reverse_lazy('blog:blog_inicio')

