'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                      //
//                         Proyecto:	Sitio WEB para Tecnología QuickMatch C.A.                       // 
//                         Fecha:		Septiembre de 2023                                              //
//                         Autor:		Francisco Reyes ©                                               //
//                         Archivo:		forms.py para Contacto                                          //
//																										//
//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

from django import forms

# Cree sus modelos aquí:

class FormularioContacto(forms.Form):
    
    nombre=forms.CharField(label="Nombre", required=True)
    
    email=forms.CharField(label="Email", required=True)
    
    contenido=forms.CharField(label="Contenido", widget=forms.Textarea)