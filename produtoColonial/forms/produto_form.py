from django import forms
from produtoColonial.models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

        # widgets = { #Configura modelo de exibição do formulario na WEB, para cada item
        #    "title": TextInput(attrs={"class": "form-control",})
        # }

    #def __init__(self, *args, **kwargs):
    #    super(ArticleForm, self).__init__(*args, **kwargs)
    #    for new_field in self.visible_fields():
    #        new_field.field.widget.attrs['class'] = 'form-control'
