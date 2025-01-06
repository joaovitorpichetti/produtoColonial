from django import forms
from produtoColonial.models import Pedido, cliente


class PedidoFormStatus(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ["status"]
