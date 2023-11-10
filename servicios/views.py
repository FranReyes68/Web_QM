'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                      //
//                         Proyecto:	Sitio WEB para Tecnología QuickMatch C.A.                       // 
//                         Fecha:		Septiembre de 2023                                              //
//                         Autor:		Francisco Reyes ©                                               //
//                         Archivo:		views.py para Servicios                                         //
//																										//
//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

from django.shortcuts import render
from servicios.models import Servicio
# Cree your Vistas aquí:

def servicios(request):
    servicios=Servicio.objects.all()
    return render(request, "servicios/servicios.html", {"servicios": servicios})