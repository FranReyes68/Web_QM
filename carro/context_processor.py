'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                      //
//                         Proyecto:	Sitio WEB para Tecnología QuickMatch C.A.                       // 
//                         Fecha:		Septiembre de 2023                                              //
//                         Autor:		Francisco Reyes ©                                               //
//                         Archivo:		Context_Procesor para Carro                                     //
//																										//
//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

def importe_total_carro(request):
    total=0
    if request.user.is_authenticated:
    #if 'carro' in request.session:                    # Línea NO incluida en programación Original
        for key, value in request.session["carro"].items():
            total=total+float(value["precio"])
            
    else:
        total = "Debe Iniciar Sesión o Registrase"
    
    
    return {"importe_total_carro":total}