

from django.urls import path
from recipes.views import contato, sobre, home

# domain/recipes/contato
urlpatterns = [
    path('contato/', contato,), #contato
    path('sobre/', sobre), #sobre
    path('', home), #home
]