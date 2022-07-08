from django.db import router
from django.urls import path, include
from .views import index, nosotros, loginCli,insert_data, registroCorrecto, contacto, registroUsuario, usuario, productos, crud, formulario, mod_prod, eliminar_prod, privacidad , registroUsuario, ProductoViewset, productito,navbar
from rest_framework import routers
# from django.conf import settings #media
# from django.conf.urls.static import static #media

router = routers.DefaultRouter()
router.register('producto', ProductoViewset)


urlpatterns = [
    path('', index, name='index'), #le quite el nombre aca para que se acceda directamente.
    path('nosotros', nosotros, name='nosotros'),
    path('contacto', contacto, name='contacto'),
    path('registroCorrecto', registroCorrecto, name='registroCorrecto'),
    path('privacidad', privacidad, name='privacidad'),
    path('usuario', usuario, name='usuario'),
    path('loginCli', loginCli, name='loginCli'),
    path('insert_data', insert_data, name='insert_data'),
    path('productos', productos, name='productos'),
    path('crud', crud, name='crud'),
    path('formulario', formulario, name='formulario'),
    path('mod_prod/<id>',mod_prod, name='mod'),
    path('eliminar_prod/<id>',eliminar_prod, name='eliminar'),
    path('registro/',registroUsuario, name='registro'),
    path('api/', include(router.urls)),
    path('productito', productito, name='productito'),
    path('navbar', navbar, name='navbar'),
    
]

#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
