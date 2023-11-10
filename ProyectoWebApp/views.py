'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                      //
//                         Proyecto:	Sitio WEB para Tecnología QuickMatch C.A.                       // 
//                         Fecha:		Septiembre de 2023                                              //
//                         Autor:		Francisco Reyes ©                                               //
//                         Archivo:		views.py para ProyectoWebApp                                    //
//																										//
//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

from django.shortcuts import render, HttpResponse
from carro.carro import Carro

# Create your views here.

def home(request):
    
    carro=Carro(request)
    
    return render(request, "ProyectoWebApp/home.html")