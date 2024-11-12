from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def calcular(request):
    return render(request, 'calculadora/pages/calcular.html')

def historico(request):
    return render(request, 'calculadora/pages/historico.html')

def sair(request):
    return HttpResponse('HOME2')

def usuario(request, id):
    return HttpResponse(f'Usuario com ID: {id}')
