from re import template
from aiohttp import request
from attr import fields
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from .models import *

import redis
import pickle


from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.views.decorators.cache import cache_page

from .models import Categoria, Lotto
from .forms import  Crea_Lotto
from django.views.generic.edit import CreateView
import socket

""""  
    Prima Vista Che Ci Permette Di Vedere A Video Tutti I Lotti
"""
class Lista_Lotti(ListView):
    queryset = Lotto.objects.all()
    template_name = 'Lista_Lotti.html'
    context_object_name = 'lotti'

"""" 
    Vista Che Ci PErmette Di Inserire I Lotti 
"""

def crea_lotto(request):
    if request.method == 'POST':
        form = Crea_Lotto(request.POST)

        if form.is_valid():

            new_lotto = form.save()

            queryset = Lotto.objects.all()

            for analisi in queryset:
                if analisi.hash == None:
                    analisi.writeOnChain()

            db = redis.StrictRedis(
                                    host = 'localhost', 
                                    port = '6379', 
                                    password='password', 
                                    db=0
                                    )
            oggetto = Lotto.objects.last()
            pickled_ogg = pickle.dumps(oggetto)
            db.set('some_key', pickled_ogg)
            unp_ogg = pickle.loads(db.get('some_key'))
            oggetto == unp_ogg

            return HttpResponseRedirect('/')
    else:
        form = Crea_Lotto()
    context = {
        'form' : form
    }
    return render(request, 'Crea_Lotti.html', context)

"""" 
    Vista Che Ci PErmette Di Inserire Nuove Categorie Per I Lotti
"""

class Crea_Categoria(CreateView):
    model = Categoria
    fields = [
        'nome',
        'descrizione'
    ]
    template_name = 'Crea_Tipologia.html'
    success_url = '/'

"""" 
    Vista Che Ci PErmette Di Effetuare ricerche
"""

def cerca(request):
    if 'q' in request.GET:
        querystrin = request.GET.get("q")
        if len(querystrin) == 0:
            return redirect("/cerca/")
        codici = Lotto.objects.filter(hash = querystrin)
        categoria = Categoria.objects.filter(nome = querystrin)
        user = User.objects.filter(username = querystrin)
        
        context = {
            'codici' : codici,
            'categoria' : categoria,
            'user' : user,
        }

        return render(request, 'cerca.html', context)
    
    else:
        return render(request, 'cerca.html')