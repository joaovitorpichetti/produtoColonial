from produtoColonial.models.base import BaseModel
from django.db import models
from produtoColonial.models.produtor import Produtor
from produtoColonial.models.categoria import Categoria

class Produto(BaseModel):
    produtor = models.ForeignKey(Produtor, on_delete=models.CASCADE,verbose_name="Produtor", help_text="Selecione o produtor responsavel pelo produto")
    nome = models.CharField(max_length=50, verbose_name="Nome do Produto", help_text="Informe um nome para o produto . (ex. Mel 300g")
    imagem = models.ImageField(verbose_name="Imagem do produto", help_text="Inclua a imagem do produto")
    categoria = models.ManyToManyField(Categoria, verbose_name="Categoria", help_text="Selecione a ou as categorias que o produto pertence")
    descricao = models.TextField(max_length=800, verbose_name="Descrição do Produto", help_text="Esse campo é destinado para informações gerais e especificas do produto")
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço", help_text="Informe o preço do produto")

    class Meta:
        abstract = False

    def __str__(self):
        return self.nome + " - " + self.produtor.nomeFantasia
