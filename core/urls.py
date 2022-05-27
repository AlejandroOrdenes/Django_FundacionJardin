from django.urls import path
from .views import index, nosotros, contacto, usuario, productos


urlpatterns = [
    path( '', index, name="index"),
    path( '', nosotros, name="nosotros"),
    path( '', contacto, name="contacto"),
    path( '', usuario, name="Usuario"),
    path( '', productos, name="Productos")
]