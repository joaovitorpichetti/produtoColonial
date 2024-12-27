from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from produtoColonial.models.pedido import Pedido

@login_required
def pedidos(request):
    pedidos = Pedido.objects.all()
    conteudo = {
        'pedidos': pedidos
    }
    return render(request, "produtoColonial/pedidos.html", conteudo)
