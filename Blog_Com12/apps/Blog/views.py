from django.shortcuts            import render,redirect
from django.urls                 import reverse_lazy
from django.views.generic        import TemplateView
from django.views.generic        import ListView, CreateView, UpdateView
from django.views.generic.edit   import UpdateView, DeleteView, FormView
from django.views.generic.detail import DetailView
from .models                     import BlogPost, BlogComentario
from .forms                      import CrearPostForm,CrearComentarioForm
from django.contrib.auth.mixins  import LoginRequiredMixin
from apps.Usuarios.mixins        import GroupRequiredMixin
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
    def get_queryset(self):
        return BlogPost.postobjects.all()
    
    
class PostNuevo(GroupRequiredMixin,CreateView):
        group_required = [u'admin', u'Escritor']
        template_name = 'Blog/blog_nuevo.html'
        model = BlogPost
        form_class = CrearPostForm
        
        def get_success_url(self, **kwargs):
         return reverse_lazy("blog:blog_inicio")

class PostEditar(GroupRequiredMixin,UpdateView):
    template_name = 'blog/post_detalle.html'
    model = BlogPost
    form_class = CrearPostForm


    def get_success_url(self, **kwargs):
        return reverse_lazy('blog/post_detalle.html')

class ComentarioNuevo(LoginRequiredMixin,CreateView):
        template_name = 'Blog/post_detalle.html'
        model = BlogComentario
        form_class = CrearComentarioForm
        
        def get_success_url(self, **kwargs):
         return reverse_lazy("blog:post_detalle")

class PostComentario(ListView):
    model = BlogComentario
    template_name = "blog/post_detalle.html"
    context_object_name = "comentarios"
    def get_queryset(self):
        return BlogComentario.objects.all()

