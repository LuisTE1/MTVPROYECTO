from django.shortcuts import render
from django.http import HttpResponse
from AppMTV.models import Familiares, Family
from datetime import datetime
# Create your views here.
def familiares(request, nombre, parentesco, celular):
    
    dia = datetime.now()

    familiares= Familiares(celular=celular, nombre=nombre, parentesco=parentesco)    
    familiares.save()
    
    return HttpResponse(
        f"""
        </p>Hoy es:<br>{dia}
        <br>Numero de celular: {familiares.celular}
        <br>De {familiares.nombre}
        <br>Que es {familiares.parentesco}
        <br>Agregado exitosamente!</p>
                        """
    )
    
def family(request, nombre, parentesco, celular, fecha_nacimiento):
    

    family= Family(celular=celular, fecha_nacimiento=fecha_nacimiento, nombre=nombre, parentesco=parentesco)    
    family.save()
    
    return HttpResponse(
        f"""
        </p>Fecha de nacimiento:<br>{family.fecha_nacimiento}
        <br>De {family.nombre}
        <br>Que es {family.parentesco}
        <br>Con Numero de celular: {family.celular}
        <br>¡¡¡¡Agregado exitosamente!!!!</p>
                        """
    )    
    
   

def lista_familiares(request):
    
    lista = Familiares.objects.all()
    
    return render(request,"lista_familia.html",{"lista_familiares": lista})

def lista_family(request):
    
    lista = Family.objects.all()
    
    return render(request,"lista_family.html",{"lista_family": lista})

def Formulario(request):
    return render(request, "Formulario.html")