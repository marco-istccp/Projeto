# encoding: utf-8
from django.shortcuts import render

def home(request):
	return render(request, 'index.html')

def sobre(request):
	return render(request, 'sobre.html')

def profilejr(request):
	return render(request, 'profilejr.html')

def profilemarco(request):
	return render(request, 'profilemarco.html')		

def ListaCursos(request):
	return render(request, 'cursos.html')