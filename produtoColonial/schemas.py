from ninja import ModelSchema

from produtoColonial.models import Produtor, Produto

class ProdutorOut(ModelSchema):
    class Meta:
        model = Produtor
        exclude = ["user", "plano"]

class ProdutoOut(ModelSchema):
    class Meta:
        model = Produto
        exclude = ["produtor"]