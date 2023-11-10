"""
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                      //
//                         Proyecto:	Sitio WEB para Tecnología QuickMatch C.A.                       // 
//                         Fecha:		Septiembre de 2023                                              //
//                         Autor:		Francisco Reyes ©                                               //
//                         Archivo:		urls.py para Servicios                                          //
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

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 

# Cree sus Vistas aquí:

urlpatterns = [
    
    path('',views.servicios,name="Servicios"),
    
]