from email.policy import default
from tabnanny import verbose
from aiohttp import request
from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse

from .utils import sendTransaction
import hashlib

class Categoria(models.Model):
    nome = models.CharField(max_length=35, null=False, blank=False, default=None)
    descrizione = models.TextField(blank=False, null=False)
    data_creazione = models.DateField(auto_now=True, blank=False, null=False)

    def __str__(self): 
        return self.nome
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorie'

class Lotto(models.Model):
    utente_creazione = models.ForeignKey(User, on_delete=models.CASCADE, related_name='utenti')
    titolo = models.CharField(max_length=35, null=False, blank=False)
    tipologia = models.ManyToManyField(Categoria)
    descrizione = models.TextField(blank=False, null=False)
    data_creazione = models.DateField(auto_now=True, blank=False, null=False)

    hash = models.CharField(max_length = 66, default = None, null = True, blank=True)
    txId = models.CharField(max_length = 66, default = None, null = True, blank=True)

    def writeOnChain(self):
        self.hash = hashlib.sha256(self.descrizione.encode('utf-8')).hexdigest()
        self.txId = sendTransaction(self.descrizione)
        self.save()

    def __str__(self):
        return self.titolo
    
    class Meta:
        verbose_name = 'Lotto'
        verbose_name_plural = 'Lotti'

    def get_absolute_url(self):
        return (reverse('dettaglio', kwargs = {"pk" : self.pk}))


        