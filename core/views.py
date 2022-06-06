
from django.shortcuts import render
from .models import Producto
from .forms import ProductoForm
# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def usuario(request):
    return render(request, 'core/Usuario.html')

def productos(request):
    return render(request, 'core/Productos.html')


def crud(request):
    #accedo al objeto que contiene los datos de la base 
    #el metodo all traera todos los productos que esten en la tablita
    productos= Producto.objects.all()
    #ahora crearemos una variable que le pase los datos del producto al template
    datos = {
        'productos': productos
    }
    #ahora se le agrega para que se envie al template de html
    return render(request, 'core/Crud.html', datos) #claro esto es solo una prueba la pagina puede cambiar
    
def formulario(request):
    datos = {
        'form': ProductoForm()
    }
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProductoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # redirect to a new URL:
            datos['mensaje'] = "Datos Guardados Correctamente"

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProductoForm()

    return render(request, 'core/formulario.html', datos)

