from django.contrib import admin
from . import models
from .models import Usuario, Contactar

admin.site.register(Usuario)

@admin.register(models.Contactar)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('subject','email',"fecha")
    search_fields = ("subject", "email","fecha")
    list_filter = ("fecha",)
    readonly_fields= ('subject','email','message',"fecha")
