from django.contrib import admin
from django.urls import path, include

from .views import registrazione_ut, home_page

urlpatterns = [
    path('Registrazione/', registrazione_ut, name='Registrazione_Ut'),
    path('home_page', home_page, name = 'home')
]
