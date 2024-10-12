# urlpatterns é utilizado para definir quais serão as rotas
# rota nada mais é do que o caminho para poder chegar a uma função
from django.urls import path

from sistema import views


urlpatterns = [
    # quando o usuário acessar o /home será executado a função
    # index do arquivo sistema/views.py
    path("/home", views.index),
    path("/", views.index),
    path("/contato", views.contato),
    path("/calculadora", views.calculadora),
    path("/calcular", views.calcular),
    path("/aluno", views.aluno),
    path("/calcular-media", views.calcular_media),
]
