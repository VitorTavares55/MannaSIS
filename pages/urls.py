from django.http import HttpRequest
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('login', LoginView.as_view(), name="login"),
    path('membros', MemberList.as_view(), name="membros"),
    path('membro', MemberView.as_view(), name="membro"),
    path('perfil/<member_id>', views.memberprofile, name="perfil"),
]
