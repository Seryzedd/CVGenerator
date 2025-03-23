from django.http import HttpResponse
from django.shortcuts import render
from apps.login.forms.login_form import LoginForm

# Create your views here.

def login_view(request):
    #return HttpResponse("Bienvenue page accueil !")
    return render(request, 'index.html', {'form': LoginForm})