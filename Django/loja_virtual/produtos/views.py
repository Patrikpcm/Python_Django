from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'produtos/index.html')

def celulares(request):
    return render(request, 'produtos/celulares.html')

def moveis(request):
    return render(request, 'produtos/moveis.html')

def notebooks(request):
    return render(request, 'produtos/notebooks.html')
