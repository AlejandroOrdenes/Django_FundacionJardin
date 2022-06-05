
from django.db import models

# Create your models here.

#Clase de usuario para uso

# class Usuario (models.Model):
#     run =models.IntegerField(primary_key=True, verbose_name='Run')
#     nombre =models.CharField(max_length=100, verbose_name='Nombre')
#     direccion =models.CharField(max_length=100, verbose_name='Direccion')
#     correoElectronico =models.CharField(max_length=100, verbose_name='Correo Electronico')
#     contraseña =models.CharField(max_length=40, verbose_name='Contraseña')
#     suscrito =models.CharField(max_length=40, verbose_name='Contraseña')

#modelo para categoria(que son plantas,maceteros,etc..)

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la Categoria')

    def __str__(self):
        return self.nombreCategoria

#modelo para el producto(que son plantas,maceteros,etc..)

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True,verbose_name='id de Producto')
    nombre_prod= models.CharField(max_length=40,verbose_name='Nombre_prod')
    imagen_prod= models.ImageField(upload_to="Productos") #python -m pip install Pillow   eso me lo pidio
    descripcion_prod= models.CharField(max_length=600,verbose_name='Descripcion')
    cantidad_prod= models.IntegerField(verbose_name='Cantidad de productos')
    precio_prod= models.IntegerField(verbose_name='Precio')
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_prod

class DetalleVenta(models.Model):
    idDetVenta = models.IntegerField(primary_key=True,verbose_name='id Detalle Venta')
    cantidad_prod_venta = models.IntegerField(verbose_name='Cantidad de productos')
    subtotal = models.IntegerField(verbose_name='Subtotal')

    def __str__(self):
        return self.idDetVenta


class Venta(models.Model):
    idVenta = models.IntegerField(primary_key=True,verbose_name='id Venta')
    fech_venta = models.DateField(verbose_name='Fecha Venta')
    descuento = models.IntegerField(verbose_name='Descuento Venta')
    subtotal = models.IntegerField(verbose_name='Subtotal')
    iva = models.IntegerField(verbose_name='Iva')
    total = models.IntegerField(verbose_name='Total')

    def __str__(self):
        return self.idVenta

class Cliente(models.Model):
    idCliente = models.IntegerField(primary_key=True,verbose_name='id Cliente')
    rut_cli = models.CharField(null=False, max_length=11,verbose_name='Rut Clienet')
    nombre_cli = models.CharField(max_length=40,verbose_name='Nombre_prod')
    email = models.CharField(max_length=40,verbose_name='Email')
    direccion = models.CharField(max_length=40,verbose_name='Direccion Cli')
    suscripcion = models.BooleanField(verbose_name='Suscripcion Cli')

    def __str__(self):
        return self.rut_cli