from produtoColonial.models.base import BaseModel
from django.db import models

class Plano(BaseModel):
    nome_plano = models.CharField(max_length=50, verbose_name="Nome do Plano", help_text="Informe o nome do Plano (Exemplo: Autoatendimento ou Cesta Juntos)")
    valor = models.FloatField(verbose_name="Valor da mensalidade", help_text="Informe o valor do plano, que deve ser paga mensalmente")
    data_de_pagamento = models.IntegerField(verbose_name="Dia do Pagamento", help_text="Informe um dia para pagamento do plano (ex. dias: 5)")

    class Meta:
        abstract = False

    def __str__(self):
        return self.nome_plano
