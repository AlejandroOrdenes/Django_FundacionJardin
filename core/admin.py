from django.contrib import admin
from .models import Categoria, Producto, DetalleVenta, Venta, Cliente
# Register your models here.
# permite administrar el modelo completo

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(DetalleVenta)
admin.site.register(Venta)
admin.site.register(Cliente)