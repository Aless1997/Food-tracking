from django import views
from django.contrib import admin
from django.urls import path

from .views import Lista_Lotti, crea_lotto, Crea_Categoria, cerca

urlpatterns = [
    path('', Lista_Lotti.as_view(), name='Lotti'),
    path('Crea_Lotti/', crea_lotto, name='creazione_lotti'),
    path('Crea_Categoria/', Crea_Categoria.as_view(), name='crea_categorie'),
    path('Cerca/', cerca, name='cerca'),
]
