from django.shortcuts            import render,redirect,reverse
from django.urls                 import reverse_lazy
from django.views.generic        import TemplateView
from django.views.generic        import ListView, CreateView, UpdateView
from django.views.generic.edit   import UpdateView, DeleteView, FormView
from django.views.generic.detail import DetailView
from .models                     import BlogPost, BlogComentario
from .forms                      import CrearPostForm, CrearComentarioForm
from django.contrib.auth.mixins  import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator       import Paginator
from braces.views                import GroupRequiredMixin
from django.db.models            import Count
from .filters                    import PostFilter
# Create your views here.
class BlogInicio(ListView):
    template_name = "Blog/blog_inicio.html"
    model = BlogPost
    context_object_name = "posts"
    paginate_by = 6
  
    def get_queryset(self):
        return BlogPost.postobjects.all()

class FiltrarFechaHoy(ListView):
    template_name = "Blog/blog_inicio.html"
    model = BlogPost
    context_object_name = "posts"
    paginate_by = 9

    def get_queryset(self):
        return BlogPost.postobjects.filter(publicado__range=["2021-12-19", "2021-12-20"])

class FiltrarCategoria(ListView):
    template_name = "Blog/blog_inicio.html"
    model = BlogPost
    context_object_name = "posts"
    paginate_by = 9

    def get_queryset(self):
        return BlogPost.postobjects.filter(categoria_id=self.kwargs.get('pk'))    

class FiltrarComentarios(ListView):
    template_name = "Blog/blog_inicio.html"
    model = BlogPost
    context_object_name = "posts"
    paginate_by = 9

    def get_queryset(self):
        return BlogPost.postobjects.annotate(comment_count=Count('comentarios')).filter(comment_count__gt=0).order_by('-comment_count')

    #def contador_comentarios(self):
      #  posts_by_score = BlogComentario.objects.filter(publicado=True).values('object_pk').annotate(
      #  score=Count('id')).order_by('-score')
      #  post_ids = [int(obj['object_pk']) for obj in posts_by_score]
      #  top_posts = Post.objects.in_bulk(post_ids)
      #  return top_posts

class PostDetalle(DetailView):
    model = BlogPost
    template_name = 'blog/post_detalle.html'
    context_object_name = 'post'
    def get_queryset(self):
        return BlogPost.objects.all()
    
    
class PostNuevo(GroupRequiredMixin,CreateView):
        group_required = [u'admin', u'Escritor']
        template_name = 'Blog/blog_nuevo.html'
        model = BlogPost
        form_class = CrearPostForm
        group_required = [u"escritor", u"admin"]
        
        
        def get_success_url(self, **kwargs):
            return reverse_lazy("blog:blog_inicio")

        def form_valid(self, form):
            f = form.save(commit=False)
            f.autor = self.request.user
            return super(PostNuevo, self).form_valid(form)

class PostEditar(UserPassesTestMixin,UpdateView):
    template_name = 'blog/blog_editar.html'
    model = BlogPost
    form_class = CrearPostForm

    def get_success_url(self, **kwargs):
        return reverse('blog:post_detalle', kwargs={'pk': self.kwargs['pk']})
    
    def test_func(self):
        obj = self.get_object()
        return obj.autor == self.request.user or self.request.user.is_superuser


    def form_valid(self, form):
        f = form.save(commit=False)
        f.autor = self.request.user
        return super(PostEditar, self).form_valid(form)

class PostEliminar(GroupRequiredMixin,UserPassesTestMixin,DeleteView):
    template_name = 'Blog/blog_eliminar.html'
    model = BlogPost
    group_required = [u"escritor", u"admin"]
    success_url = reverse_lazy('blog:blog_inicio')

    def test_func(self):
        obj = self.get_object()
        return obj.autor == self.request.user or self.request.user.is_superuser


class ComentarioNuevo(LoginRequiredMixin,CreateView):
        template_name = 'Blog/comentarios/comentario_nuevo.html'
        model = BlogComentario
        form_class = CrearComentarioForm
        
        def get_success_url(self, **kwargs):
            return reverse('blog:post_detalle', kwargs={'pk': self.kwargs['pk']})

        def form_valid(self, form):
            f = form.save(commit=False)
            form.instance.post_id = self.kwargs["pk"]
            f.nombre = self.request.user
            f.email = self.request.user
            return super(ComentarioNuevo, self).form_valid(form)

class MostrarComentario(ListView):
    model = BlogComentario
    template_name = "blog/post_detalle.html"
    context_object_name = "comentarios"
    def get_queryset(self):
        return BlogComentario.objects.all()

class ComentarioEliminar(GroupRequiredMixin,DeleteView):
    template_name = 'Blog/Comentarios/comentario_eliminar.html'
    model = BlogComentario
    group_required = [u"admin"]
    
    def get_success_url(self, **kwargs):
        return reverse('blog:blog_inicio')

