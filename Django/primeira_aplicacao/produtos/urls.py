
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index), #url que aponta pra ela mesmo (raiz)
    path('celulares/', views.celulares), #url de uma subpagina dentro de produtos, chamada de celular
    path('moveis/', views.moveis),
]