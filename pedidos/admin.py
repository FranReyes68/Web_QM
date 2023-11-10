'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                      //
//                         Proyecto:	Sitio WEB para Tecnología QuickMatch C.A.                       // 
//                         Fecha:		Septiembre de 2023                                              //
//                         Autor:		Francisco Reyes ©                                               //
//                         Archivo:		admin.py para Pedidos	                                        //
//																										//
//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

from django.contrib import admin
from .models import Pedido, LineaPedido

# Registre sus modelos aquí:

admin.site.register([Pedido, LineaPedido])