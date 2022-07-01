from django.urls import path
from .views import index, nosotros, contacto, registroUsuario, usuario, productos, crud, formulario, mod_prod, eliminar_prod, registroUsuario
# from django.conf import settings #media
# from django.conf.urls.static import static #media

urlpatterns = [
    path('', index, name='index'), #le quite el nombre aca para que se acceda directamente.
    path('nosotros', nosotros, name='nosotros'),
    path('contacto', contacto, name='contacto'),
    path('usuario', usuario, name='usuario'),
    path('productos', productos, name='productos'),
    path('crud', crud, name='crud'),
    path('formulario', formulario, name='formulario'),
    path('mod_prod/<id>',mod_prod, name='mod'),
    path('eliminar_prod/<id>',eliminar_prod, name='eliminar'),
    path('registro/',registroUsuario, name='registro'),


]

#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
