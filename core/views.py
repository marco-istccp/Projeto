# encoding: utf-8
from django.shortcuts import render

def home(request):
	return render(request, 'index.html')

def sobre(request):
	return render(request, 'sobre.html')

def ListaCursos(request):
	return render(request, 'cursos.html')	

#from models import CadastraCurso

#def ListaCurso(request):
#	MostraCursos = CadastraCurso.objects.all()
#	return render_to_response("cursos.html",{'ListaCurso': ListaCurso})