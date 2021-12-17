from django.db import models
from apps.Usuarios.models import Usuario 
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.


#Class Comentarios

class BlogCategoria(models.Model):
    name= models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        db_table ="blog_categoria"

class BlogPost(models.Model):
    
    class BlogPostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='publicado')

    options = (
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado')
    )
    categoria = models.ForeignKey(BlogCategoria, on_delete=models.PROTECT,default=1)
    titulo = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    contenido = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='publicado',null=False, unique=True)
    publicado = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name='blog_posts')
    status = models.CharField(max_length=10,choices=options,default='borrador')
    imagen = models.ImageField(default= "empty.jpg" ,null=True, blank = True)
    objects = models.Manager()
    postobjects = BlogPostObjects()

    class Meta:
        ordering = ('-publicado',)
        db_table= "blog_post"
    
    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

class BlogComentario(models.Model):

    post = models.ForeignKey(BlogPost,on_delete=models.CASCADE, related_name='comentarios')
    nombre = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    contenido = models.TextField(max_length=500)
    publicado = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    class Meta:
        ordering = ('-publicado',)
        db_table= "blog_comentario"
    
    def __str__(self):
        return f"comentado por {self.nombre}"
    