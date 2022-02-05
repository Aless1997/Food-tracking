from django.urls import path

from .views import Lista_Categorie

urlpatterns = [
    path('Lista_Categorie/', Lista_Categorie.as_view(), name= 'categorie')
]
