from django import forms
from produtoColonial.models import Cliente
from django.contrib.auth.models import User

class ClienteForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    cpf = forms.CharField(max_length=11)
    celular = forms.CharField(max_length=11)
    cep = forms.CharField(max_length=15)
    endereco = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = ['password', 'email', 'first_name', 'last_name'] #'__all__' 'password', 'username',
        #widgets = {"user":forms.HiddenInput()} #aqui escondemos o campo User

    #Metodo save para salvar o usuário e criar uma instância de Cliente
    def save(self, commit=True):
        #Chama o mtodo save do ModelForm sem ainda commitar no banco de dados
        user = super().save(commit=False)
        # Define a senha do usuário usando set_password para garantir que seja criptografada
        user.set_password(self.cleaned_data['password'])
        user.username = self.cleaned_data['email']
        if commit:
            #Salva o objeto User no banco de dados
            user.save()
            #Cria uma instância de Cliente associada ao usuário e salva no banco de dados
            Cliente.objects.create(user=user, cpf=self.cleaned_data['cpf'], celular=self.cleaned_data['celular'], cep=self.cleaned_data['cep'], endereco=self.cleaned_data['endereco'])
        return user

