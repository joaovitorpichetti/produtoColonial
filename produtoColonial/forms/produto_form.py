from django import forms
from django.contrib.auth.models import User

from produtoColonial.models import Produto, Produtor


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

        # widgets = { #Configura modelo de exibição do formulario na WEB, para cada item
        #    "title": TextInput(attrs={"class": "form-control",})
        # }

    def __init__(self, *args, **kwargs):
        user: User = kwargs.pop('user')
        super(ProdutoForm, self).__init__(*args, **kwargs)

        if user.is_staff:
            self.fields['produtor'].queryset = Produtor.objects.all()
        else:
            self.fields['produtor'].initial = Produtor.objects.get(user=user)
            self.fields['produtor'].widget = forms.HiddenInput()
