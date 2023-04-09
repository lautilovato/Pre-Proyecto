from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso, Profesor
from .forms import ProfesorForm

def crear_curso(request):
    
    nombre_curso= "Marketing"
    comision_curso= 918052

    curso= Curso(nombre= nombre_curso, comision= comision_curso)
    curso.save()
    respuesta= f"Curso creado: {nombre_curso} - {comision_curso}"
    return HttpResponse(respuesta)

def crear_profesor(request):
    
    nombre_profesor= "Franco"
    apellido_profesor= "Di Martino"
    email_profesor = "fdm@gmail.com"
    profesion_profesor = "docente"

    profesor= Profesor(nombre= nombre_profesor, apellido= apellido_profesor, email = email_profesor, profesion = profesion_profesor )
    profesor.save()
    respuesta= f"profesor creado: {nombre_profesor} - {apellido_profesor}"
    return HttpResponse(respuesta)

def cursos(request):
    return render(request, "AppCoder/cursos.html")
 
def profesores(request):
    
    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            profesor = Profesor()
            profesor.nombre = form.cleaned_data["nombre"]
            profesor.apellido = form.cleaned_data["apellido"]
            profesor.email = form.cleaned_data["email"]
            profesor.profesion = form.cleaned_data["profesion"]
            profesor.save()
            form = ProfesorForm()
    else:
            form = ProfesorForm()


    profesores = Profesor.objects.all()
    contexto = {"profesores" : profesores, "form" : form}
    return render(request, "AppCoder/profesores.html", contexto)

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")

def inicio(request):
    return HttpResponse("Bienvenido a la pagina principal")

def inicioApp(request):
    return render(request, "AppCoder/inicio.html")