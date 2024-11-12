from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('HOME')

def home1(request):
    return HttpResponse('HOME1')

def home2(request):
    return HttpResponse('HOME2')

def home3(request):
    return HttpResponse('HOME3')
