from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from produtoColonial.models.pedido import Pedido
from produtoColonial.forms.pedido_form import PedidoForm
from produtoColonial.forms.pedido_form_status import PedidoFormStatus

@login_required
def pedidos(request):
    pedidos = Pedido.objects.all()
    conteudo = {
        'pedidos': pedidos
    }
    return render(request, "produtoColonial/pedidos.html", conteudo)


@login_required
def verPedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    conteudo = {
        "pedido": pedido,
    }
    return render(request, 'produtoColonial/pedido_ver.html', conteudo)

@login_required
def editarPedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    try:
        if request.method == "POST":
            form = PedidoFormStatus(request.POST, files=request.FILES, instance=pedido)
            if form.is_valid():
                form.save()
                return redirect('aplicacao:pedidos')
        else:
            form = PedidoFormStatus(instance=pedido)
        conteudo = {
            "form": form,
            "pedido_id": pedido_id,
        }
        return render(request, 'produtoColonial/pedido_edit.html', conteudo)
    except:
        return redirect(request, 'produtoColonial/pedidos.html')
