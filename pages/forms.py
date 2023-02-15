from django import forms
from .models import *


class CustomHubForm(forms.ModelForm):
    class Meta:
        model = Hub
        fields = ['foto', 'nome', 'sede', 'regiao', 'representante', 'instituicoes', 'participantes', 'conexao', 'quantidadeAlunos', 'descricao']

class CustomInstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = ['foto', 'nome', 'email', 'telefone', 'site', 'hub', 'esfera', 'endereco', 'quantidadeAlunos', 'descricao']

class CustomMemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['foto', 'nome', 'categoria', 'bolsa', 'instituicao', 'email', 'fone', 'git', 'lattes', 'link', 'insta', 'twt', 'face', 'youtube', 'cpf', 'rg', 'genero', 'formacao', 'dtnasc', 'endereco', 'projeto', 'premio', 'nomeBanco', 'numeroBanco', 'numeroAgencia', 'numeroConta', 'termoCompromisso', 'termoCiencia', 'planoTrabalho', 'lgpd']
        widgets = {
            "dtnasc": forms.TextInput(attrs={'class':'form-control', 'type':'date'})
        }

