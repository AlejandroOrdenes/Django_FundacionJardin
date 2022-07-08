from django.contrib import admin

from core.views import usuario
from .models import Categoria, Cliente, Producto, DetalleVenta, Venta
# Register your models here.
# permite administrar el modelo completo

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(DetalleVenta)
admin.site.register(Venta)
admin.site.register(Cliente)