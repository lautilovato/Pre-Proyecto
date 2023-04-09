from django.urls import path
from .views import *

urlpatterns = [
    path('', inicioApp, name="inicioApp"),
    path('crear_curso/', crear_curso),
    path('crear_profesor/', crear_profesor),
    path('cursos/', cursos, name="cursos"),
    path('profesores/', profesores, name="profesores"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('entregales/', entregables, name="entregables"),
]