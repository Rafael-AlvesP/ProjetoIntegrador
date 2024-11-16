from django.urls import path
from django.http import HttpResponse
from calculadora import views
from . import views

urlpatterns = [
    path('calcular/', views.calcular_prazos, name='calcular'),
    path('historico/', views.historico, name='historico'), 
    path('sair/', views.sair, name='sair'),
    path('usuario/<int:id>/', views.usuario, name='usuario'),

]