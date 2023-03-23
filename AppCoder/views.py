from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso

def crear_curso(request):
    
    nombre_curso= "Redes"
    comision_curso= 100100

    curso= Curso(nombre= nombre_curso, comision= comision_curso)
    curso.save()
    respuesta= f"Curso creado: {nombre_curso} - {comision_curso}"
    return HttpResponse(respuesta)