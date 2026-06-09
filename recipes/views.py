from django.shortcuts import render
from utils import factory

def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Luiz Otávio',
        'recipes': [factory.make_recipe() for _ in range(10)]
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': factory.make_recipe(),
        'is_detail_page': True,
    })