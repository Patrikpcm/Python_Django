from django.shortcuts import render

# Create your views here.
"""
a view tem os recurso para fazer a exibição utilizando o HTML e o CSS(templates)
"""
from django.http import HttpResponse

def index(request):
    #aqui consigo fazer vários processamentos, como por exemplo recuperar dados de um BD, ANTES DE CHAMAR O RENDER
    context = {
        'nome': 'Patrik Luiz Gogola',
        'ultimo_acesso': '10/12/1989',
        'produtos': [
                        {'nome':'Notebook Acer', 'preco':'1.200,00'},
                        {'nome':'Notebook Samsung', 'preco':'2.200,00'},
                        {'nome':'Notebook Lenovo Gamer', 'preco':'8.670,00'},
                    ],
        'idade': 11,
    }

    #Chamando o render para de fato exibir a página, porém com uma terceira variável que define os dados de context
    return render(request, 'index.html', context)

def celulares(request):
    return render(request, 'celulares.html')
    #return HttpResponse('Página de celulares')

def moveis(request):
    return render(request, 'moveis.html')