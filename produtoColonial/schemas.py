from ninja import ModelSchema, Schema

from produtoColonial.models import Cliente, Pedido, Plano, Produtor, Produto

class ProdutorOut(ModelSchema):
    class Meta:
        model = Produtor
        exclude = ["user", "plano"]

class ProdutoOut(ModelSchema):
    class Meta:
        model = Produto
        exclude = ["produtor"]

class ClienteOut(ModelSchema):
    class Meta:
        model = Cliente
        fields = ["id", "user", "cpf", "celular", "cep", "endereco"]

class PedidoOut(ModelSchema):
    produtos: list[ProdutoOut] = []
    cliente: ClienteOut = None
    class Meta:
        model = Pedido
        fields = "__all__"

class PlanoOut(ModelSchema):
    class Meta:
        model = Plano
        fields = ["nome_plano", "valor", "data_de_pagamento"]

class FaturaProdutorOut(ModelSchema):
    plano: PlanoOut = None
    class Meta:
        model = Produtor
        fields = ["id", "nomeFantasia", "documento"]