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
    nombre= models.CharField(max_length=40,verbose_name='Nombre')
    #imagen= models.ImageField(upload_to="Productos") #python -m pip install Pillow   eso me lo pidio
    descripcion= models.CharField(max_length=600,verbose_name='Descripcion')
    precio= models.IntegerField(verbose_name='Precio')
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre