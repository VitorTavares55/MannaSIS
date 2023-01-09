from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div
from .models import Member

class CustomMemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['foto', 'nome', 'categoria', 'bolsa', 'instituicao', 'email', 'fone', 'git', 'cpf', 'rg', 'sexo', 'formacao', 'dtnasc', 'endereco', 'projeto', 'premio', 'nomeBanco', 'numeroBanco', 'numeroAgencia', 'numeroConta', 'termoCompromisso', 'termoCiencia', 'planoTrabalho']
        widgets = {
            "dtnasc": forms.TextInput(attrs={'class':'form-control', 'type':'date'})
        }


