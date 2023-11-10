"""
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                      //
//                         Proyecto:	Sitio WEB para Tecnología QuickMatch C.A.                       // 
//                         Fecha:		Septiembre de 2023                                              //
//                         Autor:		Francisco Reyes ©                                               //
//                         Archivo:		asgi.py                                                         //
//																										//
//////////////////////////////////////////////////////////////////////////////////////////////////////////
"""

"""
Configuración ASGI para Proyecto QM.

Expone el ASGI invocable como una variable de nivel de módulo denominada ``aplicación``.

Para más información, consulte este sitio:
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProyectoWeb.settings')

application = get_asgi_application()