'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                      //
//                         Proyecto:	Sitio WEB para Tecnología QuickMatch C.A.                       // 
//                         Fecha:		Septiembre de 2023                                              //
//                         Autor:		Francisco Reyes ©                                               //
//                         Archivo:		admin.py para Servicios                                         //
//																										//
//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

from django.contrib import admin
from .models import Servicio

# Registre sus modelos aquí:

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('created','update')


admin.site.register(Servicio, ServicioAdmin)