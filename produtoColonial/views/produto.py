from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from produtoColonial.decorators import produtor_only
from produtoColonial.models import Categoria
from produtoColonial.models.produto import Produto
from produtoColonial.forms.produto_form import ProdutoForm
from django.contrib.auth.decorators import login_required

@login_required
def lista_produtor(request, ):
    produtos = Produto.objects.filter(produtor__user=request.user)
    conteudo = {
        "produtos": produtos
    }

    return render(request, "produtoColonial/produtos_lista_produtor.html", conteudo)
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
            return redirect("aplicacao:produtos_lista_produtor")
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
        return redirect('aplicacao:produtos_lista_produtor')
    except:
        context = {
        }
        return render(request, "produtoColonial/produtos_lista_produtor.html", context)


class ProdutoListView(ListView):
    model = Produto
    template_name = 'produtoColonial/produtos_lista.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoria_id = self.request.GET.get('c')
        termo_pesquisa = self.request.GET.get('q')

        context['categorias'] = Categoria.objects.all()

        produto_list = Produto.objects.all()

        if termo_pesquisa is not None:
            produto_list = produto_list.filter(nome__icontains=termo_pesquisa)

        if categoria_id is not None:
            context['categoria_selecionada'] = Categoria.objects.get(pk=categoria_id)
            produto_list = produto_list.filter(categoria=categoria_id)

        context['produto_list'] = produto_list

        return context
