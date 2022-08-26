from django.shortcuts import render, redirect
from .models import Curso
# Create your views here.
def home(request):
    cursoListado = Curso.objects.all()
    return render(request, "gestionCursos.html", {"cursos": cursoListado})

def registrarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    
    curso = Curso.objects.create(codigo=codigo, nombre=nombre)
    
    return redirect('/')