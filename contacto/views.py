'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                      //
//                         Proyecto:	Sitio WEB para Tecnología QuickMatch C.A.                       // 
//                         Fecha:		Septiembre de 2023                                              //
//                         Autor:		Francisco Reyes ©                                               //
//                         Archivo:		views.py para Contacto                                          //
//																										//
//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Cree sus Vistas aquí:

def contacto(request):
    formulario_contacto=FormularioContacto()
    
    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")
            
            
            email=EmailMessage("Correo procedente desde el sitio Web de QM",
            "El Usuario: {}, cuyo Correo es: {}, nos ha enviado el siguiente Mensaje:\n\n {}".format(nombre,email,contenido),
            "",["sitio.web.qm@gmail.com"],reply_to=[email])
            
            try:
                email.send()

                return redirect("/contacto/?Válido")
            except:
                return redirect("/contacto/?Inválido")


    return render(request, "contacto/contacto.html", {'miFormulario':formulario_contacto})