from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    email = models.EmailField(max_length=100)
    class Meta:
        db_table = 'usuarios'
