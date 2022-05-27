from django.shortcuts import render

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

