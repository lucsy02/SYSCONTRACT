from django.urls import path
from .views import cadastrar_cliente, listar_clientes

urlpatterns = [
    path('cadastro/', cadastrar_cliente, name='cadastro'),
    path('clientes/', listar_clientes, name='clientes'),
]
