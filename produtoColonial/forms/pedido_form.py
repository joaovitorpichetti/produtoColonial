from django import forms
from produtoColonial.models import Pedido, Produto

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'
