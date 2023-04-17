from django.db import models

class Curso(models.Model):
    nombre= models.CharField(max_length= 50) # campo de texto
    comision= models.IntegerField() # campo de numeros
    def __str__(self):
        return f"{self.nombre} - {self.comision}"

class Estudiante(models.Model):
    nombre= models.CharField(max_length= 50)
    apellido= models.CharField(max_length= 40)
    email= models.EmailField() # campo de tipo email
    def __str__(self):
        return f"{self.nombre} - {self.apellido} "
    
class Profesor(models.Model):
    nombre= models.CharField(max_length= 50)
    apellido= models.CharField(max_length= 50)
    email= models.EmailField()
    profesion= models.CharField(max_length= 50)
    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.email} - {self.profesion}"

class Entregable(models.Model):
    nombre= models.CharField(max_length= 50)
    fecha= models.DateField() # campo de tipo fecha 
    entregado= models.BooleanField() # campo de tipo bool