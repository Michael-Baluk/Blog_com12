from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):

    class Meta:
        db_table = 'usuarios'
