from django.shortcuts import render, get_object_or_404, redirect
from produtoColonial.forms.cliente_form import ClienteForm
from django.contrib.auth import login

def cadastro(request):
    if request.method == 'POST':
        #print("Chegou os dados")
        #print(request.POST)
        form = ClienteForm(request.POST)
        #print(form.is_valid())
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio') # Redirecionar para a página inicial ou outra página após o login
        print(form.errors)
        return render(request, 'produtoColonial/cadastro_clientes.html', {'form': form})
    else:
        form = ClienteForm()
    return render(request, 'produtoColonial/cadastro_clientes.html', {'form': form})
