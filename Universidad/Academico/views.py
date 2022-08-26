from django.shortcuts import render
from .models import Curso
# Create your views here.
def home(request):
    cursoListado = Curso.objects.all()
    return render(request, "gestionCursos.html", {"cursos": cursoListado})