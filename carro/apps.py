"""
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                      //
//                         Proyecto:	Sitio WEB para Tecnología QuickMatch C.A.                       // 
//                         Fecha:		Septiembre de 2023                                              //
//                         Autor:		Francisco Reyes ©                                               //
//                         Archivo:		apps.py para Carro                                              //
//																										//
//////////////////////////////////////////////////////////////////////////////////////////////////////////
"""

from django.apps import AppConfig


class CarroConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'carro'