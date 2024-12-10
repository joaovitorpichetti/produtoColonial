from django.shortcuts import render, get_object_or_404, redirect
from produtoColonial.models.produto import Produto
from produtoColonial.forms.produto_form import ProdutoForm
from django.contrib.auth.decorators import login_required

@login_required
def lista(request):
    produtos = Produto.objects.all()
    conteudo = {
        "produtos": produtos
    }

    return render(request, "produtoColonial/produtos_lista.html", conteudo)
