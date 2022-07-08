from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from rest_framework import viewsets
from .serializers import CategoriaSerializer, ProductoSerializer


# Create your views here.

class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


    def get_queryset(self):
        productos = Producto.objects.all()

        nombre = self.request.GET.get('nombre')

        if nombre:
            productos = productos.filter(nombre_prod__contains=nombre)
        
        return productos


def index(request):
    return render(request, 'core/index.html')

def registroUsuario(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login(request, user)
            messages.success(request, "Registrado Correctamente")
            return redirect(to="index")
        data["form"] = formulario
    return render(request, 'registration/register.html', data)

def nosotros(request):
    return render(request, 'core/nosotros.html')

def privacidad(request):
    return render(request, 'core/politicaPrivacidad.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def usuario(request):
    return render(request, 'core/Usuario.html')

def productos(request):
    #accedo al objeto que contiene los datos de la base 
    #el metodo all traera todos los productos que esten en la tablita
    productos= Producto.objects.all()
    #ahora crearemos una variable que le pase los datos del producto al template
    datos = {
        'productos': productos
    }
    #ahora se le agrega para que se envie al template de html
    return render(request, 'core/Productos.html', datos)


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
    data = {
        'form': ProductoForm()
    }
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProductoForm(data=request.POST, files=request.FILES) 
        # check whether it's valid:
        if form.is_valid():
            form.save()
            messages.success(request, "Agregado Correctamente")
        else:
            data["form"] = formulario
    return render(request, 'core/formulario.html', data)


def mod_prod(request, id):
    producto = get_object_or_404(Producto, idProducto=id)
    #ahora crearemos una variable que le pase los datos del producto al template
    datos = {
        'form': ProductoForm(instance=producto)
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="crud")
        datos["form"] = formulario

    return render(request, 'core/mod.html', datos)

def eliminar_prod(request, id):
    producto = get_object_or_404(Producto, idProducto=id)
    producto.delete()
    messages.success(request, "eliminado correctamente")
    return redirect(to="crud")
def productito(request):
    #accedo al objeto que contiene los datos de la base 
    #el metodo all traera todos los productos que esten en la tablita
    productos= Producto.objects.all()
    #ahora crearemos una variable que le pase los datos del producto al template
    datos = {
        'productos': productos
    }
    #ahora se le agrega para que se envie al template de html
    return render(request,'core/Productito.html', datos)
def navbar(request):
    return render(request, 'core/navBar.html')
