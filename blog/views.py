'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                      //
//                         Proyecto:	Sitio WEB para Tecnología QuickMatch C.A.                       // 
//                         Fecha:		Septiembre de 2023                                              //
//                         Autor:		Francisco Reyes ©                                               //
//                         Archivo:		views.py para Blog		                                        //
//																										//
//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

from django.shortcuts import render
from blog.models import Post, Categoria

# Cree sus Vistas aquí:

def blog(request):
    posts=Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts})

def categoria(request, categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)
    return render(request, "blog/categoria.html", {'categoria':categoria, "posts": posts})