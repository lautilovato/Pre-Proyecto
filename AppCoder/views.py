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

def cursos(request):
    return render(request, "AppCoder/cursos.html")
 
def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")

def inicio(request):
    return HttpResponse("Bienvenido a la pagina principal")

def inicioApp(request):
    return render(request, "AppCoder/inicio.html")