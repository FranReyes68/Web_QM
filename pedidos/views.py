'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                      //
//                         Proyecto:	Sitio WEB para Tecnología QuickMatch C.A.                       // 
//                         Fecha:		Septiembre de 2023                                              //
//                         Autor:		Francisco Reyes ©                                               //
//                         Archivo:		views.py para Pedidos                            	            //
//																										//
//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

from django.contrib.auth.decorators import login_required
from carro.carro import Carro
from pedidos.models import LineaPedido, Pedido
from .models import Producto
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.

@login_required(login_url="/autenticacion/logear")
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user)	# Damos de Alta un Pedido
    carro=Carro(request)							# Tomamos el Carro
    lineas_pedido=list()							# Lista con los Pedidos para recorrer los elementos del Carro
    for key, value in carro.carro.items():			# Recorremos el Carro con sus items
        lineas_pedido.append(LineaPedido(
            producto_id=key,
            cantidad=value['cantidad'],
            user=request.user,
            pedido=pedido
			))
    
    LineaPedido.objects.bulk_create(lineas_pedido)	# Crea registros en BD en Paquete
    # Enviamos E-mail al Cliente:
    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.user.username,
        email_usuario=request.user.email
    )
    # Mensaje Posterior al Envío:
    messages.success(request, "¡Su Pedido se ha creado Correctamente!")
    
    return redirect("../tienda")

def enviar_mail(**kwargs):
    asunto="¡Gracias por su Compra!"
    mensaje=render_to_string("emails/pedido.html", {
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombreusuario": kwargs.get("nombreusuario")
		})
    
    mensaje_texto=strip_tags(mensaje)
    from_email="sitio.web.qm@gmail.com"
    #to=kwargs.get("emailusuario")
    to="jose.francisco.reyes@gmail.com"
    send_mail(asunto,mensaje_texto,from_email,[to],html_message=mensaje)