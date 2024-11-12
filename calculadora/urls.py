from django.urls import path
from django.http import HttpResponse
from calculadora.views import home, home1, home2, home3

urlpatterns = [
    path('', home),
    path('historico/', home1),
    path('sair/', home2),
    path('usuario/', home3),

]