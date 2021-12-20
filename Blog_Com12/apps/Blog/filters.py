import django_filters 

from .models import *

class PostFilter(django_filters.FilterSet):
    class Meta:
        model: BlogPost
        fields: ['categoria','publicado']