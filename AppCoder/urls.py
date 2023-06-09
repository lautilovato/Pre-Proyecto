from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicioApp, name="inicioApp"),
    path('crear_curso/', crear_curso),
    path('crear_profesor/', crear_profesor),
    path('cursos/', cursos, name="cursos"),
    path('profesores/', profesores, name="profesores"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('entregales/', entregables, name="entregables"),
    path('busqueda_comision/', busqueda_comision, name="busqueda_Comision"),
    path('buscar/', buscar, name= "buscar"),
    path('elminar_profesor/<id>', eliminar_profesor, name= "eliminar_profesor"),
    path('editar_profesor/<id>', editar_profesor, name= "editar_profesor"),
    path("estudiante/list/", Estudiante_list.as_view(), name="estudiante_list"),
    path('estudiante/nuevo/', EstudianteCreacion.as_view(), name="estudiante_crear"),
    path('estudiante/<pk>', EstudianteDetalle.as_view(), name="estudiante_detalle"),
    path('estudiante/editar/<pk>', EstudianteUpdate.as_view(), name="estudiante_editar"),
    path('estudiante/borrar/<pk>', EstudianteDelete.as_view(), name="estudiante_borrar"),
    path('login/', login_request, name= "login"),
    path('register/', register, name="register"),
    path('logout/', LogoutView.as_view(), name= "logout"), # otra opcion: LogoutView.as_view(template_name= "AppCoder/logout.html")
    path('editar_perfil/', editar_perfil, name= "editar_perfil"),
    path('agregar_avatar/', agregar_avatar, name= "agregar_avatar" ),
]
