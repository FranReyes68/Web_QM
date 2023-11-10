'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                      //
//                         Proyecto:	Sitio WEB para Tecnología QuickMatch C.A.                       // 
//                         Fecha:		Septiembre de 2023                                              //
//                         Autor:		Francisco Reyes ©                                               //
//                         Archivo:		admin.py para Tienda                                            //
//																										//
//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

from django.contrib import admin
from .models import CategoriaProd, Producto

# Registre sus modelos aquí:

class CategoriaProdAdmin(admin.ModelAdmin):
    
    readonly_fields = ("created", "update")


class ProductoAdmin(admin.ModelAdmin):
    
    readonly_fields = ("created", "update")

admin.site.register(CategoriaProd, CategoriaProdAdmin)

admin.site.register(Producto, ProductoAdmin)