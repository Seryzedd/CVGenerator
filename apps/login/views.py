from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def login_view(request):
    #return HttpResponse("Bienvenue page accueil !")
    return render(request, 'index.html')