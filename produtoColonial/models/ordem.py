from produtoColonial.models.base import BaseModel
from django.db import models
from produtoColonial.models.cliente import Cliente
from produtoColonial.models.produto import Produto

class Ordem(BaseModel):
    status_opcoes = [
        ('ops1', 'Não Tratado'),
        ('ops2', 'Em andamento'),
        ('ops3', 'Enviado'),
        ('ops4', 'Entregue'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente", help_text="Selecione o Cliente que fez a compra")
    produtos = models.ManyToManyField(Produto, verbose_name="Selecione os produtos comprados", help_text="Neste campo você deve selecionar os produtos que o cliente compro")
    status = models.CharField(max_length=20, choices=status_opcoes, default='ops1', verbose_name="Status", help_text="Selecione o andamento da Ordem")

    class Meta:
        abstract = False

    def __str__(self):
        return self.cliente.nome + " (Status: " + self.status + " )"
