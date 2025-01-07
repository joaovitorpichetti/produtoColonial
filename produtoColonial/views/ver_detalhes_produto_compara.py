from django.shortcuts import render, get_object_or_404, redirect
from produtoColonial.models.produto import Produto

def ver_detalhes(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    conteudo = {
        "produto": produto,
    }

    return render(request, "produtoColonial/produto_detalhes.html", conteudo)
