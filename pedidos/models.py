'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                      //
//                         Proyecto:	Sitio WEB para Tecnología QuickMatch C.A.                       // 
//                         Fecha:		Septiembre de 2023                                              //
//                         Autor:		Francisco Reyes ©                                               //
//                         Archivo:		models.py para Pedidos   	                                    //
//																										//
//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

from django.db import models
from django.db.models import F,Sum, FloatField	# Para Calcular el Total de una Orden de Pedido
from tabnanny import verbose
from django.contrib.auth import get_user_model	# Devuelve el Usuario Activo Actual
from tienda.models import Producto

# Cree sus modelos aquí:

User=get_user_model()

class Pedido(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)	# Cuando se elimine un Usuario, sus Pedidos se Eliminirán en Cascada.
    created_at=models.DateTimeField(auto_now_add=True)		# Para la Fecha de Pedido Automática.
    
    @property
    def total(self):
        return self.lineapedido_set.aggregate(

            total=Sum(F("precio")*F("cantidad"), output_field=FloatField())

        )["total"] or FloatField(0)

    def __str__(self):
        return self.id


    class Meta:
        db_table='pedidos'
        verbose_name='Pedido'
        verbose_name_plural='Pedidos'
        ordering=['id']


class LineaPedido(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE) 
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido=models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cantidad} de {self.producto.nombre}'

    class Meta:
        db_table='lineapedidos'
        verbose_name='Línea Pedido'
        verbose_name_plural='Líneas Pedidos'
        ordering=['id']