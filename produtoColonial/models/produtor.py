from produtoColonial.models.base import BaseModel
from django.db import models
from django.contrib.auth.models import User
from produtoColonial.models.plano import Plano
#from django.contrib.auth.models import AbstractUser, Group, Permission

class Produtor(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Selecione o user do Produtor")
    nomeFantasia = models.CharField(max_length=50, verbose_name="Nome Fantasia", help_text="Informe o nome fantasia")
    nome = models.CharField(max_length=50, verbose_name="Nome do produtor", help_text="Informe o nome do Produtor")
    documento = models.CharField(max_length=14, verbose_name="CPF/CNPJ", help_text="Informe um documento do produtor, CPF ou CNPJ, será usado para fazer cobrança de mensalidade")
    celular = models.CharField(max_length=11, verbose_name="Celular", help_text="Informe o Celular do produtor")
    #email = models.CharField(max_length=50, verbose_name="E-mail", help_text="Informe o e-mail do produtor, será usado para fazer login")
    cep = models.CharField(max_length=15, verbose_name="CEP", help_text="Informe o CEP do endereço do Cliente")
    endereco = models.CharField(max_length=150, verbose_name="Endereço", help_text="Informe a Rua, Número da casa, Bairro e Cidade")
    plano = models.ForeignKey(Plano, on_delete=models.CASCADE, verbose_name="Plano", help_text="Selecione o plano que o produtor vai adiquirir, lembrando que os pagamentos são mensais")
    observacoes = models.TextField(max_length=500, blank=True, verbose_name="Observações", help_text="Utilize esse campo caso queira adicionar alguma observação")
    #groups = models.ManyToManyField(Group, related_name='produtor_set', blank=True)
    #user_permissions = models.ManyToManyField(Permission, related_name='produtor_permission_set', blank=True)

    class Meta:
        abstract = False
        verbose_name = "Produtor"
        verbose_name_plural = "Produtores"

    def __str__(self):
        return self.nomeFantasia
