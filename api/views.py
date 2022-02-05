from django.http import JsonResponse
from django.shortcuts import render
from Lotto.models import *

def sviluppatore(request):
    return render(request, 'Sviluppatore.html')

def api_lotto(request):
    response = []
    apis = Lotto.objects.filter().order_by('data_creazione')
    for api in apis:
        response.append(
            {
                'Titolo': api.titolo,
                'Descrizione': api.descrizione,
                'Data Creazione': api.data_creazione,
                'Hash': api.hash,
                'TxId': api.txId,

            }
        )
    return JsonResponse(response)

def api_categoria(request):
    response = []
    cats = Categoria.objects.filter().order_by('data_creazione')
    for categoria in cats:
        response.append(
            {
                'Nome' : categoria.nome,
                'data' : categoria.data_creazione,

            }
        )
    return JsonResponse(response)