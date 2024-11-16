from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PrazoForm

def calcular_prazos(request):
    if request.method == 'POST':
        form = PrazoForm(request.POST)
        if form.is_valid():
            prazo = form.save(commit=False)
            return redirect('historico') 
    else:
        form = PrazoForm()

    return render(request, 'calculadora/pages/calcular.html', {'form': form})

def historico(request):
    return render(request, 'calculadora/pages/historico.html')

def sair(request):
    return render(request, 'authors/pages/register_view.html')

def usuario(request, id):
    return HttpResponse(f'Usuario com ID: {id}')

def sucesso(request):
    return HttpResponse('Cadastro realizado com sucesso!')

def calcular(request):
    
    return render(request, 'authors/pages/register_view.html', {'form': form})


def calcular_prazos(request):
    if request.method == 'POST':
        form = PrazoForm(request.POST)
        if form.is_valid():
            prazo = form.save(commit=False)
            return redirect('historico') 
    mail = EmailMessege(
        subject="Prazo Tempo Fácil",
        body="Olá, quero lembrar que hoje, data:" {% form 'prazos/{dataFicto}' %} " está próximo do evento na data" {% form 'prazos/{dataFinal}' %} " com o nome de:" {% form 'prazos/{evento}' %}. 
        from_email="tempo.facil@outlook.com",
        to=[{% form 'usuario/{email}' %}]
    )
    mail.send()
    return render(request, 'calculadora/pages/calcular.html', {'form': form})