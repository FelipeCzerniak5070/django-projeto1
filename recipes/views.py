from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Felipe'
    })

def sobre(request):
    return render(request, 'recipes/sobre.html')

def contato(request):
    return render(request, 'recipes/contato.html')