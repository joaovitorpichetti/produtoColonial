from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from produtoColonial.decorators import produtor_only
from produtoColonial.models import Categoria
from produtoColonial.models.produto import Produto
from produtoColonial.forms.produto_form import ProdutoForm
from django.contrib.auth.decorators import login_required

@login_required
def lista_produtor(request):
    produtos = Produto.objects.all()
    conteudo = {
        "produtos": produtos
    }

    return render(request, "produtoColonial/produtos_lista.html", conteudo)
@login_required
def ver(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    conteudo = {
        "produto": produto
    }
    return render(request, 'produtoColonial/produto_ver.html', conteudo)

@produtor_only
def atualizar(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    try:
        if request.method == "POST":
            form = ProdutoForm(request.POST, files=request.FILES, instance=produto, user=request.user)
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
        return redirect(request, 'produtoColonial/produtos_lista_produtor.html')

@produtor_only
def criar(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            return redirect("aplicacao:produtos_lista")
    else:
        form = ProdutoForm(user=request.user)

    context = {
        "form": form
    }
    return render(request, "produtoColonial/produto_criar.html", context)
@produtor_only
def excluir(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    try:
        produto.delete()
        return redirect('aplicacao:produtos_lista')
    except:
        context = {
        }
        return render(request, "produtoColonial/produtos_lista.html", context)


class ProdutoListView(ListView):
    model = Produto
    template_name = 'produtoColonial/produtos_lista.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoria_id = self.request.GET.get('c')

        context['categorias'] = Categoria.objects.all()

        print(categoria_id)

        if categoria_id is not None:
            context['categoria_selecionada'] = Categoria.objects.get(pk=categoria_id)
            context['produto_list'] = Produto.objects.filter(categoria=categoria_id)
        else:
            context['produto_list'] = Produto.objects.all()

        print(context)

        return context
