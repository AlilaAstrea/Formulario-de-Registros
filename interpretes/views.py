from django.shortcuts import render
from .models import Interprete

# FUNCION PARA MOSTRAR LA PAGINA INDEX
def mostrarIndex(request):
    return render(request,"index.html")

# FUNCION PARA MOSTRAR EL LISTADO DE INTERPRETES
def mostrarListado(request):
    solistas = Interprete.objects.all().filter(clasificacion='Solista')
    bandas = Interprete.objects.all().filter(clasificacion='Banda')
    datos = {
        'solistas':solistas,
        'bandas' : bandas
    }
    return render(request,"listado.html",datos)

def eliminarInterprete(request, id):
    try:
        inter = Interprete.objects.get(id=id)
        inter.delete()
        solistas = Interprete.objects.all().filter(clasificacion='Solista')
        bandas = Interprete.objects.all().filter(clasificacion='Banda')
        datos = {
            'solistas':solistas,
            'bandas' : bandas,
            'msg':'Se elimino con exito el interprete'
        }
        return render(request,"listado.html",datos)
    except:
        solistas = Interprete.objects.all().filter(clasificacion='Solista')
        bandas = Interprete.objects.all().filter(clasificacion='Banda')
        datos = {
            'solistas':solistas,
            'bandas' : bandas,
            'error':'Error, no se logro eliminar el interprete.'
        }
        return render(request,"listado.html",datos)



def mostrarFormRegistrar(request):
    
    return render(request,"form_registrar.html")


def registrarInterprete(request):   
    nom = request.POST['txtnom']     ## Recuperamos la información
    gen = request.POST['cbogen']
    cla = request.POST['opcla']
    apa = request.POST['txtapa']
    inter = Interprete(nombre=nom, genero=gen, clasificacion=cla, aparicion=apa)
    inter.save()  # guardamos en la bd
    
    datos ={
        'msg':'Se registro con exito el nuevo interprete'
    }
    
    return render(request, "form_registrar.html", datos)  # guarda los datos, falta imprimir el mensaje


def mostrarFormActualizar(request, id):
    try:
        
        inter = Interprete.objects.get(id=id)   # inter posee todos los datos del id #buscamos el interprete que tenga el id el cual queremos editar ( el que se envia)
        fecha = inter.aparicion
        dia = str(fecha.day)
        if fecha.day <= 9:
            dia ="0"+str(fecha.day)
            
        mes = str(fecha.month)
        if fecha.month <=9:
            mes ="0"+str(fecha.month)
        
        año = str(fecha.year)    # str lo convierte en texto ya que daria problemas por ser un dato numerico
        fecha = año + "-" + mes + "-" + dia
        
        datos = {
            'inter':inter,
            'fecha':fecha,
        }
        return render(request,"form_actualizar.html",datos)  # esto ocurre si el interprete encuentra el id 
    except:
        solistas = Interprete.objects.all().filter(clasificacion='Solista')
        bandas = Interprete.objects.all().filter(clasificacion='Banda')
        datos = {
            'solistas':solistas,
            'bandas' : bandas,
            'error':'Error, no se logro editar el interprete.'
        }
        return render(request,"listado.html",datos)
    
    
    
def actualizarInterprete(request, id):
    try:
        nom = request.POST['txtnom']
        gen = request.POST['cbogen']
        cla = request.POST['opcla']
        apa = request.POST['txtapa']
        inter = Interprete.objects.get(id=id) 
        inter.nombre = nom
        inter.genero = gen
        inter.clasificacion = cla
        inter.aparicion = apa
        inter.save()
        
        solistas = Interprete.objects.all().filter(clasificacion='Solista')
        bandas = Interprete.objects.all().filter(clasificacion='Banda')
        datos = {
            'solistas':solistas,
            'bandas' : bandas,
            'msg':'Ok, Interprete modificado cone exito'
        }
        return render(request,"listado.html",datos)
        
        
    except:
        solistas = Interprete.objects.all().filter(clasificacion='Solista')
        bandas = Interprete.objects.all().filter(clasificacion='Banda')
        datos = {
            'solistas':solistas,
            'bandas' : bandas,
            'error':'Error, no se logro actualizar el interprete.'
        }
        return render(request,"listado.html",datos)
        
    