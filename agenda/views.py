# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required

from models import ItemAgenda
from forms import FormItemAgenda
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext

@login_required
def lista(request):
    lista_itens = ItemAgenda.objects.filter(usuario=request.user)
    return render_to_response("lista.html", {'lista_itens': lista_itens}, context_instance=RequestContext(request))


@login_required
def adiciona(request):
    if request.method == 'POST': # Formulário enviado
        form = FormItemAgenda(request.POST, request.FILES)
        if form.is_valid():
            # Formulário válido.
            item = form.save(commit=False)
            item.usuario = request.user
            item.save()

            # Mensagem de formulário cadastrado
            return render_to_response("salvo.html", {})
    else:
        # Exibe formulário em branco
        form = FormItemAgenda()

    return render_to_response("adiciona.html", {'form': form}, context_instance=RequestContext(request))

@login_required
def item(request, nr_item):
    item = get_object_or_404(ItemAgenda, usuario=request.user, id=nr_item)
    if request.method == "POST":
        form = FormItemAgenda(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return render_to_response("salvo.html", {})
    else:
        form = FormItemAgenda(instance=item)
    return render_to_response("item.html", {'form': form}, context_instance=RequestContext(request))

@login_required
def remove(request, nr_item):
    item = get_object_or_404(ItemAgenda, usuario=request.user, id=nr_item)
    if request.method == "POST":
        item.delete()
    	return render_to_response("removido.html", {'item': item},
    		context_instance=RequestContext(request))
    else:
        return render_to_response("remove.html", {'item': item},
        	context_instance=RequestContext(request))