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

def examen(request):
    # Información de los estudiantes y sus repositorios de GitHub
    estudiantes = [
        {"Marjorie Luque": "Estudiante 01", "github": "https://github.com/MarjorieLuque/EC3_LUQUECARDENAS.git"},
        {"Roxana Pascacio": "Estudiante 02", "github": "https://github.com/roxana0315/UC3-Parte02"},
        {"Jhonny Tenorio": "Estudiante 03", "github": " https://github.com/Jten202/UC3-Parte03.git"},
        {"Marjorie Luque": "Estudiante 04", "github": "https://github.com/MarjorieLuque/UC3_PARTE4_LUQUE.git"},
        
    ]

    context = {"estudiantes": estudiantes}
    return render(request, 'miapp/examen.html', context)
    