from produtoColonial.models.base import BaseModel
from django.db import models
from django.contrib.auth.models import User

class Cliente(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Selecione o user do Cliente", help_text="Selecione um usuario para o cliente.")
    nome = models.CharField(max_length=50, verbose_name="Nome", help_text="Insira o nome do Cliente")
    sobrenome = models.CharField(max_length=50, verbose_name="Sobrenome", help_text="Insira o sobrenome do Cliente")
    cpf = models.CharField(max_length=11, verbose_name="CPF", help_text="Informe o CPF do Cliente (obs. só números")
    email = models.EmailField(verbose_name="E-mail", help_text="Informe o email do cliente")
    celular = models.CharField(max_length=11, verbose_name="Celular", help_text="Informe o celular do cliente com o DDD")
    cep = models.CharField(max_length=15, verbose_name="CEP", help_text="Informe o CEP do endereço do Cliente")
    endereco = models.CharField(max_length=150, verbose_name="Endereço", help_text="Informe a Rua, Número da casa, Bairro e Cidade")

    class Meta:
        abstract = False

    def __str__(self):
        return self.nome + self.sobrenome
