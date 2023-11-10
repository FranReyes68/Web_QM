'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                      //
//                         Proyecto:	Sitio WEB para Tecnología QuickMatch C.A.                       // 
//                         Fecha:		Septiembre de 2023                                              //
//                         Autor:		Francisco Reyes ©                                               //
//                         Archivo:		admin.py para Blog 	                                            //
//																										//
//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

from django.contrib import admin
from .models import Categoria, Post

# Registre sus modelos aquí:

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'update')


class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'update')


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)