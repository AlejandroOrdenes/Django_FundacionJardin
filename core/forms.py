from django import forms
from django.forms import ModelForm
from .models import Producto

#Creamos nuestra clase para el formulario desde la base de datos
class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        fields =['idProducto','nombre','descripcion','precio', 'categoria']

#no cacho porque no me toma el formulario la verdad, me perdi maomeno
#hasta aca la ppt 3.2.2 en la pag 14
