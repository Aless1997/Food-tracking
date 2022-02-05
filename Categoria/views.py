from django.shortcuts import render

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from Lotto.models import Categoria

class Lista_Categorie(ListView):
    queryset = Categoria.objects.all()
    template_name = 'Lista_Categorie.html'
    context_object_name = 'categoria'