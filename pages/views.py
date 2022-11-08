from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Member
from django import forms
from django.shortcuts import get_object_or_404

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
