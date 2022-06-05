from django import forms


#Creamos nuestra clase para el formulario desde la base de datos
class ProductoForm(forms.Form):
    nombre_prod= forms.CharField(label='Nombre Producto',max_length=40)
    imagen_prod= forms.ImageField(label='Imagen Producto') 
    descripcion_prod= forms.CharField(label='Descripción Producto', max_length=600)
    cantidad_prod= forms.IntegerField(label='Cantidad Producto')
    precio_prod= forms.IntegerField(label='Precio Producto')
    categoria = forms.CharField(label='Categoria Producto')

#no cacho porque no me toma el formulario la verdad, me perdi maomeno
#hasta aca la ppt 3.2.2 en la pag 14
