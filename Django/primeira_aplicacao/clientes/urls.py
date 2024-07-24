
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index), #url que aponta pra ela mesmo (raiz)
    path('emails/', views.emails), #url que aponta para um subdominio dentro de emails
]