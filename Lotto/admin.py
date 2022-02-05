from django.contrib import admin
from .models import Categoria, Lotto

admin.site.register(Lotto)
admin.site.register(Categoria)

class LottoModelAdmin(admin.ModelAdmin):
    model = Lotto
    list_display = ['utente_creazione', 'tipologia','data_creazione']
    search_field = ['utente_creazione', 'tipologia']
    list_filter = ['data_creazione', 'utente_creazione']


