'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                      //
//                         Proyecto:	Sitio WEB para Tecnología QuickMatch C.A.                       // 
//                         Fecha:		Septiembre de 2023                                              //
//                         Autor:		Francisco Reyes ©                                               //
//                         Archivo:		views.py para Tienda                                            //
//																										//
//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

from django.shortcuts import render
from .models import Producto

# Cree sus Vistas aquí:

def tienda(request):
    
    productos = Producto.objects.all()
    
    return render(request, "tienda/tienda.html", {"productos":productos})