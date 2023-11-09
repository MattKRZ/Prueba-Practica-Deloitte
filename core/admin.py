from django.contrib import admin
from .models import Productos, Categorias

# Register your models here.
admin.site.register(Productos)
admin.site.register(Categorias)