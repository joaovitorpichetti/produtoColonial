from django.shortcuts import render, get_object_or_404, redirect
from produtoColonial.models.produto import Produto
from produtoColonial.forms.produto_form import ProdutoForm

def lista(request):
    produtos = Produto.objects.all()
    conteudo = {
        "produtos": produtos
    }

    return render(request, "produtoColonial/produtos_lista.html", conteudo)
