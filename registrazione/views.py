from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

from .form import FormRegistrazione

# Create your views here.
def home_page(request):
    return render(request, 'base.html')

def registrazione_ut(request):
    if request.method == "POST":
        form = FormRegistrazione(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            User.objects.create_user(
                username = username,
                password = password,
                email=email,
            )
            user = authenticate(
                username=username,
                password=password,
            )
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = FormRegistrazione()
    
    context = {
        'form' : form,
    }
    return render(request, 'Registrazione.html', context)