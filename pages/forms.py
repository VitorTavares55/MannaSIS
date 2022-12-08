from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div
from .models import Member

class CustomMemberForm(forms.ModelForm):
    foto = forms.ImageField(required=True, label=("Foto"))
    nome = forms.CharField(required=True, label=("Nome Completo"))
    categoria = forms.CharField(required=True, label=("Categoria"))
    bolsa = forms.CharField(required=True, label=("Bolsa"))
    instituicao = forms.CharField(required=True, label=("Instituição"))
    email = forms.CharField(required=True, label=("E-mail"))
    fone = forms.CharField(required=True, label=("Fone"))
    git= forms.CharField(required=True, label=("Usuário GIT"))
    cpf = forms.CharField(required=True, label=("CPF"))
    rg = forms.CharField(required=True, label=("RG"))
    sexo = forms.CharField(required=True, label=("Sexo"))
    formacao = forms.CharField(required=True, label=("Formação"))
    dtnasc = forms.CharField(required=True, label=("Data de Nascimento"))
    endereco = forms.CharField(required=True, label=("Endereço"))
    projeto = forms.CharField(required=True, label=("Projeto"))
    premio = forms.CharField(required=True, label=("Prêmio"))
    nomeBanco = forms.CharField(required=True, label=("Nome do Banco"))
    numeroBanco = forms.CharField(required=True, label=("Número do Banco"))
    numeroAgencia = forms.CharField(required=True, label=("Número da Agência"))
    numeroConta = forms.CharField(required=True, label=("Número da Conta"))
    termoCompromisso = forms.FileField(required=True, label=("Termo de Compromisso"))
    class Meta:
        model = Member
        fields = ['foto', 'nome', 'categoria', 'bolsa', 'instituicao', 'email', 'fone', 'git', 'cpf', 'rg', 'sexo', 'formacao', 'dtnasc', 'endereco', 'projeto', 'premio', 'nomeBanco', 'numeroBanco', 'numeroAgencia', 'numeroConta', 'termoCompromisso']


