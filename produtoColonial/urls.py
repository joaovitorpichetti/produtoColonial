from django.urls import path
from . import views

app_name = 'aplicacao'

urlpatterns = [
    path('produto/', views.lista, name='produtos_lista'),
    path('produto/ver/<int:produto_id>', views.ver, name='produto_ver'),
    path('produto/atualizar/<int:produto_id>', views.atualizar, name='produto_atualizar'),
    path('produto/excluir/<int:produto_id>', views.excluir, name='produto_excluir'),
    path('produto/criar', views.criar, name='produto_criar'),
    path('cadastro/cliente', views.cadastro, name='cadastro_cliente'),
]
