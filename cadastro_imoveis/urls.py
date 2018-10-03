from django.urls import path
from .views import (criar_imovel,ImovelListView,lista_imoveis)

urlpatterns = [
     path('add/',criar_imovel,name='cria_imovel'),
     path('',ImovelListView.as_view(),name='lista_imovel'),
     path('imoveis/',lista_imoveis,name='imoveis')
]