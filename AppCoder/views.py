from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


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

@login_required
def cursos(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = Curso()
            curso.nombre = form.cleaned_data["nombre"]
            curso.comision = form.cleaned_data["comision"]
            curso.save()
            form = CursoForm()
    else:
            form = CursoForm()

    cursos = Curso.objects.all()
    contexto = {"cursos" : cursos, "form" : form}
    return render(request, "AppCoder/cursos.html", contexto)

@login_required
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

def editar_profesor(request, id):
    profesor=Profesor.objects.get(id=id)
    if request.method=="POST":
        form= ProfesorForm(request.POST)
        if form.is_valid():
            
            info=form.cleaned_data
            
            profesor.nombre=info["nombre"]
            profesor.apellido=info["apellido"]
            profesor.email=info["email"]
            profesor.profesion=info["profesion"]

            profesor.save()
            profesores=Profesor.objects.all()
            form = ProfesorForm()
            return render(request, "AppCoder/Profesores.html" ,{"profesores":profesores, "mensaje": "Profesor editado correctamente", "form": form})
        pass
    else:
        formulario= ProfesorForm(initial={"nombre":profesor.nombre, "apellido":profesor.apellido, "email":profesor.email, "profesion":profesor.profesion})
        return render(request, "AppCoder/editar_profesor.html", {"form": formulario, "profesor": profesor})


def eliminar_profesor(request, id):
    profesor=Profesor.objects.get(id=id)
    print(profesor)
    profesor.delete()
    profesores=Profesor.objects.all()
    form = ProfesorForm()
    return render(request, "AppCoder/Profesores.html", {"profesores": profesores, "mensaje": "Profesor eliminado correctamente", "form": form})

@login_required
def estudiantes(request):
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            estudiante = Estudiante()
            estudiante.nombre = form.cleaned_data["nombre"]
            estudiante.apellido = form.cleaned_data["apellido"]
            estudiante.email = form.cleaned_data["email"]
            estudiante.save()
            form = EstudianteForm()
    else:
            form = EstudianteForm()
    
    estudiantes = Estudiante.objects.all()
    contexto = {"estudiantes" : estudiantes, "form" : form}
    return render(request, "AppCoder/estudiantes.html", contexto)
@login_required
def entregables(request):
    return render(request, "AppCoder/entregables.html")

def inicio(request):
    return HttpResponse("Bienvenido a la pagina principal")

def inicioApp(request):
    return render(request, "AppCoder/inicio.html")

def busqueda_comision(request):
    return render(request, "AppCoder/busqueda_comision.html")

def buscar(request):
    
    comision= request.GET["comision"]
    if comision!="":
        cursos= Curso.objects.filter(comision__icontains=comision)#buscar otros filtros en la documentacion de django
        return render(request, "AppCoder/resultadosBusqueda.html", {"cursos": cursos})
    else:
        return render(request, "AppCoder/busquedaComision.html", {"mensaje": "Che Ingresa una comision para buscar!"})

# vistas basadas en clases

class Estudiante_list(LoginRequiredMixin, ListView):
    model = Estudiante
    template_name = "AppCoder/estudiantes.html"

class EstudianteCreacion(LoginRequiredMixin, CreateView):#vista usada para CREAR
    model= Estudiante
    success_url= reverse_lazy("estudiante_list")
    fields=['nombre', 'apellido', 'email']

class EstudianteDetalle(LoginRequiredMixin, DetailView): #vista usada para MOSTRAR DATOS
    model=Estudiante
    template_name="Appcoder/estudiante_detalle.html"

class EstudianteDelete(LoginRequiredMixin, DeleteView):#vista usada para ELIMINAR
    model=Estudiante
    success_url= reverse_lazy("estudiante_list")

class EstudianteUpdate(LoginRequiredMixin, UpdateView):#vista usada para EDITAR
    model = Estudiante
    success_url = reverse_lazy('estudiante_list')
    fields=['nombre', 'apellido', 'email']

# login, logout register

def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            info=form.cleaned_data
            
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave)#verifica si el usuario existe, si existe, lo devuelve, y si no devuelve None 
            
            if usuario is not None:
                login(request, usuario)
                return render(request, "AppCoder/inicio.html", {"mensaje":f"EL Usuario {usu} ha iniciado sesion correctamente"})
            else:
                return render(request, "AppCoder/login.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, "AppCoder/login.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request, "AppCoder/login.html", {"form": form})
    
def register(request):
    if request.method=="POST":
        form= RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render(request, "AppCoder/inicio.html", {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "AppCoder/register.html", {"form": form, "mensaje":"Error al crear el usuario"})
    else:
        form= RegistroUsuarioForm()
        return render(request, "AppCoder/register.html", {"form": form})