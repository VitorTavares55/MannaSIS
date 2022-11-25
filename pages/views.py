from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Member
from django import forms
from django.shortcuts import get_object_or_404, render
from .forms import MemberForm

# Create your views here.

class IndexView(TemplateView):
    template_name = "pages/index.html"

class LoginView(TemplateView):
    template_name = "pages/login.html"

##class MemberList(LoginRequiredMixin, ListView):
class MemberList(ListView):
	#login_url = reverse_lazy('login')
	model = Member
	template_name = 'pages/member-list.html'
	#success_url = reverse_lazy('index')

class MemberView(TemplateView):
	template_name = 'pages/member-profile.html'


def memberprofile(request, member_id):
    get=get_object_or_404(Member, pk=member_id) 
    return render(request,'pages/member-profile.html',{'member': get})

def membercreate(request):
	context = {'form' : MemberForm()}
	return render(request, 'pages/form.html', context)

class MemberCreate(CreateView):
	model = Member
	fields = ['foto', 'nome', 'categoria', 'bolsa', 'instituicao', 'email', 'fone', 'git', 'cpf', 'rg', 'sexo', 'formacao', 'dtnasc', 'endereco', 'projeto', 'premio', 'nomeBanco', 'numeroBanco', 'numeroAgencia', 'numeroConta', 'termoCompromisso']
	template_name = 'pages/form.html'
