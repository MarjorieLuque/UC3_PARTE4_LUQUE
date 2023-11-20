from django.shortcuts import render

from sympy import primerange

def home(request):
    
    context = {

        'title': 'UNTELS',
        'content': 'Este es tu contenido personalizado.',
    }
    return render(request, 'miapp/home.html', context)

