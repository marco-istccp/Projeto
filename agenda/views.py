#encoding: utf-8

from django.shortcuts import render_to_response

from django.template import RequestContext

from models import ItemAgenda

from forms import FormItemAgenda

def lista(request):
	lista_itens = ItemAgenda.objects.all()
	return render_to_response("lista.html",
	 	{'lista_itens': lista_itens})

def adiciona(request):
#	if request.method == 'POST': # Formulario enviado
#		form = FormItemAgenda(request.POST, request.FILES)
#		if form.is_valid():
#
#			# Formulario Valido
#			dados = form.cleaned_data
#			item = ItemAgenda(data=dados['data'],
#				hora=dados['hora'],
#				titulo=dados['titulo'],
#			descricao=dados['descricao'])
#			item.save()
#
#			# Mensagem de formulario cadastrado
#			return render_to_response("salvo.html",{})
#
#	else: # pagina acessada via link (metodo GET)		
#		# exibe formulario em branco
#		form = FormItemAgenda()

	if request.method == 'POST': # Formulario enviado
		form = FormItemAgenda(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response("salvo.html", {})	
	else:
		form = FormItemAgenda()
	return render_to_response("adiciona.html",{'form':form},context_instance=RequestContext(request))	

#def item(request, nr_item):
#	try:
#		item = ItemAgenda.objects.get(pk=nr_item)	
#	except ItemAgenda.DoesNotExist:
#		raise Http404()
#	return render_to_response('item.html', {'item': item})		

def item(request, nr_item):
	item = get_object_or_404(ItemAgenda, pk=nr_item) 
	if request.method == "POST":
		form = FormItemAgenda(request.POST, request.FILES, instance=item)
		if form.is_valid():
			form.save()
			return render_to_response("salvo.html", {})
	else:
		form = FormItemAgenda(instance=item)		
	return render_to_response("item.html", {'form': form}, context_instance=RequestContext())	

