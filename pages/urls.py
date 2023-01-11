from django.http import HttpRequest
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('login', LoginView.as_view(), name="login"),
    path('membros', MemberList.as_view(), name="membros"),
    path('cadastro-membro', MemberCreate.as_view(), name="cadastro-membro"),
    path('editar-membro/<int:pk>/', MemberUpdate.as_view(), name="editar-membro"),
    path('deletar-membro/<int:pk>/', MemberDelete.as_view(), name="deletar-membro"),
    path('filtro-membro', views.memberfilter, name="filtro-membro"),
    path('<member_nome>', views.memberprofile, name="membro"),
]
