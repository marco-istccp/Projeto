# encoding: utf-8

from django.shortcuts import render_to_response

from models import CadastraCurso

def ListaCurso(request):
	MostraCursos = CadastraCurso.objects.all()
	return render_to_response("Cursos.html",{'ListaCurso': ListaCurso})
