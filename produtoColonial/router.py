from ninja import Router
from ninja.security import HttpBearer

from produtoColonial.models import Pedido, Produto, Produtor
from produtoColonial.models.admin_token import AdminToken
from produtoColonial.schemas import PedidoOut, ProdutoOut, ProdutorOut

class TokenAuth(HttpBearer):
    def authenticate(self, request, token):
        try:
            user = AdminToken.objects.get(key=token).user
            return user
        except AdminToken.DoesNotExist:
            return None

router = Router(auth=TokenAuth())

@router.get("/produtores", response=list[ProdutorOut])
def get_produtores(request):
    produtores = Produtor.objects.all()
    return [ProdutorOut.from_orm(produtor) for produtor in produtores]


@router.get("/{produtor_id}/produtos", response=list[ProdutoOut])
def get_produtos_by_produtor(request, produtor_id: int):
    produtor = Produtor.objects.get(id=produtor_id)
    return produtor.produto_set.all()

@router.get("/produtos", response=list[ProdutoOut])
def get_produtos(request):
    return Produto.objects.all()

@router.get("/{produtor_id}/pedidos", response=list[PedidoOut])
def get_pedidos_by_produtor(request, produtor_id: int):
    return Pedido.objects.filter(produtor_id=produtor_id)

@router.get("/validar")
def validar(request):
    return {"valido": True}