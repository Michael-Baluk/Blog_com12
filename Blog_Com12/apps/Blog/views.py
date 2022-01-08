from django.shortcuts            import render,redirect,reverse
from django.urls                 import reverse_lazy
from django.views.generic        import TemplateView
from django.views.generic        import ListView, CreateView, UpdateView
from django.views.generic.edit   import UpdateView, DeleteView, FormView
from django.views.generic.detail import DetailView
from .models                     import BlogPost, BlogComentario, BlogCategoria
from .forms                      import CrearPostForm, CrearComentarioForm, PostFilterForm
from django.contrib.auth.mixins  import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator       import Paginator
from braces.views                import GroupRequiredMixin
from django.db.models            import Count
from bootstrap_modal_forms.generic import BSModalCreateView
from django.contrib import messages
# Create your views here.
class BlogInicio(ListView):
    template_name = "Blog/blog_inicio.html"
    model = BlogPost
    context_object_name = "posts"
    paginate_by = 6
  
    def get_context_data(self, **kwargs):
        context = super(BlogInicio, self).get_context_data(**kwargs)
        busqueda_titulo = self.request.GET.get("titulo", None)
        busqueda_categoria = self.request.GET.get("categoria", None)
        busqueda_autor = self.request.GET.get("autor", None)

        initial_data = {}
        if busqueda_titulo is not None and busqueda_titulo!="":
            initial_data["titulo"] = busqueda_titulo

        if busqueda_categoria is not None and busqueda_categoria!="":
            initial_data["categoria"] = busqueda_categoria

        context["form_filtro"] = PostFilterForm(initial=initial_data)
        return context

    def get_queryset(self):
        busqueda_titulo = self.request.GET.get("titulo", None)
        busqueda_categoria = self.request.GET.get("categoria", None)
        query = BlogPost.objects.all().order_by("-publicado")
        
        if busqueda_titulo is not None and busqueda_titulo!="":
            query = query.filter(titulo__icontains=busqueda_titulo)
        if busqueda_categoria is not None and busqueda_categoria!="":
            query = query.filter(categoria=busqueda_categoria)

        return query



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


class ComentarioNuevo(LoginRequiredMixin,BSModalCreateView):
        template_name = 'Blog/comentarios/comentario_nuevo.html'
        model = BlogComentario
        form_class = CrearComentarioForm
        raise_exception = True
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

class ComentarioEliminar(GroupRequiredMixin,LoginRequiredMixin,DeleteView):
    template_name = 'Blog/Comentarios/comentario_eliminar.html'
    model = BlogComentario
    group_required = [u"admin"]
    
    def get_success_url(self, **kwargs):
        return reverse('blog:blog_inicio')
        

