from django.shortcuts import render
from produtoColonial.models.categoria import Categoria
from produtoColonial.models.produto import Produto

def index(request):
    categoria_id = request.GET.get('c')

    conteudo = {

    }

    #conteudo = super().get_context_data(**kwargs)

    conteudo['categorias'] = Categoria.objects.all()

    print(categoria_id)

    if categoria_id is not None:
        conteudo['categoria_selecionada'] = Categoria.objects.get(pk=categoria_id)
        conteudo['produto_list'] = Produto.objects.filter(categoria=categoria_id)
    else:
        conteudo['produto_list'] = Produto.objects.all()

    print(conteudo)

    #return conteudo
    return render(request, 'conteudo.html', conteudo)