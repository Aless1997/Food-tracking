from attr import fields
from django.forms import forms
from django.db import models
from django.forms import BaseModelFormSet
from .models import Lotto, Categoria
from django import forms

class Crea_Lotto(forms.ModelForm):

    class Meta:
        model = Lotto
        fields = [
            'utente_creazione',
            'titolo',
            'tipologia',
            'descrizione',
        ]

