from django.shortcuts import render, get_object_or_404, redirect
from produtoColonial.models.produto import Produto

def verDetalher(request):
    produtos = Produto.objects()
    conteudo = {
        "produtos": produtos,
    }

    return render(request, "produtoColonial/produto_detalhes.html", conteudo)

