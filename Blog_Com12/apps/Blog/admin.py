from django.contrib import admin
from . import models

@admin.register(models.BlogPost)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('titulo','id','status','autor')
    prepopulated_fields = {'slug': ('titulo',),}

@admin.register(models.BlogComentario)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('post','nombre','email','publicado',)
    list_filter = ("status","publicado")
    search_fields = ("nombre", "email","contenido")

admin.site.register(models.BlogCategoria)
# Register your models here.
