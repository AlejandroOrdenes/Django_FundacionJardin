from django.urls import path
from .views import index, nosotros, contacto, usuario, productos


urlpatterns = [
    path('index', index, name='index'),
    path('nosotros', nosotros, name='nosotros'),
    path('contacto', contacto, name='contacto'),
    path('usuario', usuario, name='usuario'),
    path('productos', productos, name='productos')
]