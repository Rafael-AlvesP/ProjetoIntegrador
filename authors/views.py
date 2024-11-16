from django.shortcuts import render, redirect
from .forms import UsuarioForm
from django.core.mail import EmailMessage

def register_view(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            return redirect('calcular')
    else:
        form = UsuarioForm()

    return render(request, 'authors/pages/confirmacao.html', {'form': form})

def register_view(request):
    mail = EmailMessege(
        subject="Confirmação E-mail tempo fácil",
        body="E-mail de confirmação de usuário. Acesse o link para confirmar o seu cadastro https//tempofacil.com.br/confirmar/YxIkgdspP?weNBpM",
        from_email="tempo.facil@outlook.com",
        to=[{% form 'usuario/{email}' %}]
    )
    mail.send()
    return render(request, 'authors/pages/confirmacao.html', {'form': form})

def confirm(request):
    return render(request, 'authors/pages/confirmacao.html')

def terms(request):
    return render(request, 'authors/pages/termos.html')

def confirm(request):
    return render(request, 'authors/pages/termos.html')