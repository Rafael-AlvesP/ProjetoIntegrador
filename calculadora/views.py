from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PrazoForm
from bs4 import BeautifulSoup
from .models import Holiday

def calcular_prazos(request):
    if request.method == 'POST':
        form = PrazoForm(request.POST)
        if form.is_valid():
            prazo = form.save(commit=False)
            return redirect('historico') 
    else:
        form = PrazoForm()

    return render(request, 'calculadora/pages/calcular.html', {'form': form})

def get_holidays_from_site(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')


    holidays = []
    for holiday in soup.select('.holiday-class'):
        date = holiday.select_one('.date-class').text.strip()
        name = holiday.select_one('.name-class').text.strip()
        holidays.append({'date': date, 'name': name})
    
    return holidays

def save_holidays_to_db(holidays):
    for holiday in holidays:
        Holiday.objects.get_or_create(date=holiday['data'], name=holiday['feriado'])

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

    def calcular_prazos(request):
    if request.method == 'POST':
        form = PrazoForm(request.POST)
        if form.is_valid():
            prazo = form.save(commit=False)
            return redirect('historico') 
    mail = EmailMessege(
        subject="Prazo Tempo Fácil",
        body="Olá, quero lembrar que hoje" {% form 'prazos/{dataFinal}' %} "há um evento com o nome de:" {% form 'prazos/{evento}' %}. 
        from_email="tempo.facil@outlook.com",
        to=[{% form 'usuario/{email}' %}]
    )
    mail.send()
    return render(request, 'calculadora/pages/calcular.html', {'form': form})