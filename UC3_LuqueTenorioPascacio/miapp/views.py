from django.shortcuts import render,redirect
from .models import Curso
from sympy import primerange
from django.contrib import messages

def home(request):
    
    context = {

        'title': 'UNTELS',
        'content': 'Este es tu contenido personalizado.',
    }
    return render(request, 'miapp/home.html', context)

def primos(request):
    return render(request,"miapp/primos.html")

