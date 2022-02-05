from django.contrib import admin
from django.urls import path

from .views import Dettaglio_User, Dettaglio_Transazione, Lista_Utenti

urlpatterns = [
    path('Dettaglio_user/<int:pk>', Dettaglio_User.as_view(), name='user'),
    path('Dettaglio_Transazione/<int:pk>', Dettaglio_Transazione.as_view(), name='dettaglio'),
    path('Lista_Utenti/', Lista_Utenti.as_view(), name='Lista_ut')
]
 