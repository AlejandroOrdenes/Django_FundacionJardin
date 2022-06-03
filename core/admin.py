from django.contrib import admin
from .models import Categoria, Producto
# Register your models here.
# permite administrar el modelo completo

admin.site.register(Categoria)
admin.site.register(Producto)