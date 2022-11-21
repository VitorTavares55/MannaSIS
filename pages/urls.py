from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('login', LoginView.as_view(), name="login"),
    path('membros', MemberList.as_view(), name="membros"),
    path('membro', MemberView.as_view(), name="membro"),
]
