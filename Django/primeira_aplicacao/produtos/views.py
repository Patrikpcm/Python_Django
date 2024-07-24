from django.shortcuts import render

# Create your views here.
"""
a view tem os recurso para fazer a exibição utilizando o HTML e o CSS(templates)
"""
from django.http import HttpResponse

def pagina_produtos(request):
    return HttpResponse('Página de produtos')

def celulares(request):
    return HttpResponse('Página de celulares')