from produtoColonial.models.base import BaseModel
from django.db import models

class Categoria(BaseModel):
    nome = models.CharField(max_length=50, verbose_name="Nome da Categoria", help_text="Informe o nome da categoria")

    class Meta:
        abstract = False

    def __str__(self):
        return self.nome
