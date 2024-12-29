from django.contrib import messages
from django.shortcuts import redirect, render


def produtor_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if hasattr(request.user, 'produtor'):
            if getattr(request.user, 'produtor'):
                return view_func(request, *args, **kwargs)
        else:
            messages.add_message(request, messages.ERROR, 'Você não tem permissão para acessar essa página')
            return redirect("inicio")
    return wrapper_func

def cliente_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if hasattr(request.user, 'cliente'):
            if getattr(request.user, 'cliente'):
                return view_func(request, *args, **kwargs)
        else:
            messages.add_message(request, messages.ERROR, 'Você não tem permissão para acessar essa página')
            return redirect("inicio")
    return wrapper_func