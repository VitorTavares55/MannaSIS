from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView

from .models import Status

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="users/register.html", context={"register_form":form})

class StatusList(LoginRequiredMixin, ListView):
	model = Status
	template_name = 'users/user-list.html'

class StatusUpdate(LoginRequiredMixin, UpdateView):
	model = Status
	template_name = 'users/user-form.html'
	fields = ['auth', 'division']
	success_url = reverse_lazy('user-list')

def is_header(user):
    return user.groups.filter(name='Lider').exists()

def is_director(user):
    return user.groups.filter(name='Diretoria').exists()