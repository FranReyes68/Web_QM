"""
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                      //
//                         Proyecto:	Sitio WEB para Tecnología QuickMatch C.A.                       // 
//                         Fecha: 		Septiembre de 2023                                              //
//                         Autor:		Francisco Reyes ©                                               //
//                         Archivo:		wsgi.py de ProyectoWeb                                          //
//																										//
//////////////////////////////////////////////////////////////////////////////////////////////////////////

Expone el WSGI invocable como una Variable de Nivel de módulo llamada ``aplicación``.

Para más Información de este Archivo, consulte:
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProyectoWeb.settings')

application = get_wsgi_application()