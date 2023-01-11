from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Member
from django import forms
from django.shortcuts import get_object_or_404, render
from .forms import CustomMemberForm

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

def memberfilter(request):
    if request.method == 'POST':
        value = request.POST['search']
        result = Member.objects.filter(nome__contains=value)
        return render(request, 'pages/member-filter.html', {'result':result})
    else:
        return render(request, 'pages/member-list.html', {})

def memberprofile(request, member_nome):
    get=get_object_or_404(Member, nome=member_nome) 
    return render(request,'pages/member-profile.html',{'member': get})

class MemberCreate(CreateView):
    form_class = CustomMemberForm
    template_name = 'pages/form.html'
    model = Member
    success_url = reverse_lazy('membros')

class MemberUpdate(UpdateView):
    form_class = CustomMemberForm
    template_name = 'pages/form.html'
    model = Member
    success_url = reverse_lazy('membros')

class MemberDelete(DeleteView):
    template_name = 'pages/delete.html'
    model = Member
    success_url = reverse_lazy('membros')

