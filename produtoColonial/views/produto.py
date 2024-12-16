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

def ver(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    conteudo = {
        "produto": produto
    }
    return render(request, 'produtoColonial/produto_ver.html', conteudo)

def atualizar(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    try:
        if request.method == "POST":
            form = ProdutoForm(request.POST, instance=produto, user=request.user)
            if form.is_valid():
                form.save()
                # TODO: message
                return redirect('aplicacao:produtos_lista')
        else:
            form = ProdutoForm(instance=produto, user=request.user)
            context = {
                "form": form,
                "produto_id": produto_id
            }
            return render(request, 'produtoColonial/produto_edit.html', context)
    except:
        # TODO: message
        return redirect(request, 'produtoColonial/produtos_lista.html')

def criar(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect("aplicacao:produtos_lista")
    else:
        form = ProdutoForm(user=request.user)

    context = {
        "form": form
    }
    return render(request, "produtoColonial/produto_criar.html", context)

def excluir(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    try:
        produto.delete()
        return redirect('aplicacao:produtos_lista')
    except:
        context = {
        }
        return render(request, "produtoColonial/produtos_lista.html", context)
