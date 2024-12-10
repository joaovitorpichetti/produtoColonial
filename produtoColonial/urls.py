from django.urls import path
from . import views

app_name = 'aplicacao'

urlpatterns = [
    path('produto/', views.lista, name='produtos_lista'),
    path('cadastro/cliente', views.cadastro, name='cadastro_cliente'),
]
