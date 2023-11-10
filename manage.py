"""
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                      //
//                         Proyecto:	Sitio WEB para Tecnología QuickMatch C.A.                       // 
//                         Fecha:		Septiembre de 2023                                              //
//                         Autor:		Francisco Reyes ©                                               //
//                         Archivo:		manage.py                                                       //
//////////////////////////////////////////////////////////////////////////////////////////////////////////
"""

#!/usr/bin/env python
"""Utilidad de Línea de Comandos de Django para Tareas Administrativas."""
import os
import sys


def main():
    """ Iniciar Tareas Adminsitartivas. """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProyectoWeb.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()