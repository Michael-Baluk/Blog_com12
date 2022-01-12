from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Usuario(AbstractUser):
    email = models.EmailField(max_length=100)
    imagen = models.ImageField(default="empty.jpg",null=True, blank=True)
    resumen = models.TextField(max_length=250,null=True)
    class Meta:
        db_table = 'usuarios'

class Contactar(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    subject= models.CharField(max_length=250)
    message = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)
    class Meta:
        db_table = "Contacto"
    
    def __str__(self):
        return self.subject
