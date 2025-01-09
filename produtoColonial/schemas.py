from ninja import ModelSchema

from produtoColonial.models import Cliente, Pedido, Produtor, Produto

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