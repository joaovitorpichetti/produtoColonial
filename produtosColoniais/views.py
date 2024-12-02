from django.shortcuts import render

def index(request):
    conteudo = {

    }
    return render(request, 'conteudo.html', conteudo)
