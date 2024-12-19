from django.contrib import admin
from produtoColonial.models.plano import Plano
from produtoColonial.models.produtor import Produtor
from produtoColonial.models.cliente import Cliente
from produtoColonial.models.categoria import Categoria
from produtoColonial.models.produto import Produto
from produtoColonial.models.pedido import Pedido

# Register your models here.
admin.site.register(Plano)
admin.site.register(Produtor)
admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Pedido)