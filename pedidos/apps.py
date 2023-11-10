'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                      //
//                         Proyecto:	Sitio WEB para Tecnología QuickMatch C.A.                       // 
//                         Fecha:		Septiembre de 2023                                              //
//                         Autor:		Francisco Reyes ©                                               //
//                         Archivo:		apps.py para Pedidos                                        	//
//																										//
//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

from django.apps import AppConfig


class PedidosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pedidos'
