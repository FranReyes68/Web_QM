"""
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                      //
//                         Proyecto:	Sitio WEB para Tecnología QuickMatch C.A.                       // 
//                         Fecha:		Septiembre de 2023                                              //
//                         Autor:		Francisco Reyes ©                                               //
//                         Archivo:		urls.py de ProyectoWeb                                          //
//																										//
//////////////////////////////////////////////////////////////////////////////////////////////////////////

La Lista `urlpatterns` enruta las URL a las Vistas. Para obtener más información, consulte:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Ejemplos:
Vistas de Función
    1. Agregar una Importación: Desde las Vistas de Importación de my_app
    2. Agregue una URL a urlpatterns: Ruta ('', vistas.inicio, nombre = 'inicio')
Vistas basadas en Clases
    1. Añadir una Importación: from other_app.views import Home
    2. Agregar una URL a urlpatterns: ruta('', Inicio.as_view(), nombre='inicio')
Incluir otra URLconf
    1. Importe la Función include(): desde django.urls import include, ruta
    2. Agregar una URL a urlpatterns: ruta('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('servicios/', include('servicios.urls')),
    path('blog/', include('blog.urls')),
    path('contacto/', include('contacto.urls')),
    path('autenticacion/', include('autenticacion.urls')),
    path('tienda/', include('tienda.urls')),
    path('carro/', include('carro.urls')),
    path('pedidos/', include('pedidos.urls')),
    path('', include('ProyectoWebApp.urls')),

]