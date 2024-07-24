from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'clientes/index.html')

def emails(request):
    return render(request, 'clientes/email.html')