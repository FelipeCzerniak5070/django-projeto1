from django.shortcuts import render
from utils import factory

def get_recipe():
    return factory.make_recipe()

def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Felipe Czerniak',
        'recipes': [get_recipe() for _ in range(10)]
    })


def recipe(request):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': get_recipe(),
        'is_detail_page': True,
    })
    
    
    