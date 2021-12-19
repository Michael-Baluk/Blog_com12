from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    email = models.EmailField(max_length=100)
    imagen = models.ImageField(default="empty.jpg",null=True, blank=True)
    resumen = models.CharField(max_length=250,null=True)
    class Meta:
        db_table = 'usuarios'
