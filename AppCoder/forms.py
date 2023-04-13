from django import forms

class ProfesorForm(forms.Form):
    nombre= forms.CharField(max_length= 50)
    apellido= forms.CharField(max_length= 50)
    email= forms.EmailField()
    profesion= forms.CharField(max_length= 50)

class CursoForm(forms.Form):
    nombre= forms.CharField(max_length= 50)
    comision= forms.CharField(max_length= 50)

class EstudianteForm(forms.Form):
    nombre = forms.CharField(max_length= 50)
    apellido = forms.CharField(max_length= 50)
    email = forms.CharField(max_length= 50)