from django.shortcuts import render

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.contrib.auth.models import User

import socket

from Lotto.models import *

"""
    Classe che ci permetterà di andare a visualizzare tutti 
    i dettagli di un user
"""

class Dettaglio_User(DetailView):
    queryset = User.objects.all()
    template_name = 'Dettaglio_User.html'
    context_object_name = 'User'
    ip = socket.gethostbyname(socket.gethostname())
    print(ip)
    a = User.objects.all()
    for b in a:
        c = b.lista_ip

    last_ip = c[-1]

    context = {
        'last_ip' : last_ip
    }
    
"""
    Classe che ci permetterà di andare a visualizzare tutti 
    i dettagli di un lotto
"""
class Dettaglio_Transazione(DetailView):
    queryset = Lotto.objects.all()
    template_name = 'Dettaglio_Lotto.html'
    context_object_name = 'Lotto'
"""
    Classe che ci permetterà di andare a visualizzare tutti 
    gli utenti registrati
"""
class Lista_Utenti(ListView):
    queryset = User.objects.all()
    template_name = 'Lista_Utenti.html'
    context_object_name = 'utenti'

 