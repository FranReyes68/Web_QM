'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                      //
//                         Proyecto:	Sitio WEB para Tecnología QuickMatch C.A.                       // 
//                         Fecha:		Septiembre de 2023                                              //
//                         Autor:		Francisco Reyes ©                                               //
//                         Archivo:		urls.py para Blog		                                        //
//																										//
//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

from django.urls import path
from . import views

# Cree sus Vistas aquí:

urlpatterns = [
    
    path('',views.blog,name="Blog"),
    path('categoria/<int:categoria_id>/', views.categoria, name="categoria")
    
]