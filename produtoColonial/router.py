from ninja import Router
from produtoColonial.models import Produtor
from produtoColonial.schemas import ProdutorOut

router = Router()

@router.get("/produtores", response=list[ProdutorOut])
def get_produtores(request):
    produtores = Produtor.objects.all()
    return [ProdutorOut.from_orm(produtor) for produtor in produtores]
