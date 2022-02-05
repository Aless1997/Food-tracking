from unicodedata import name
from django.contrib import admin
from django.urls import path

from .views import api_lotto, sviluppatore, api_categoria

urlpatterns = [
    path('Api_Lotto/', api_lotto, name='api_lotto'),
    path('Modalità_Sviluppatore/', sviluppatore, name='sviluppatore'),
    path('Api_Categoria/', api_categoria, name='api_categoria')
]

