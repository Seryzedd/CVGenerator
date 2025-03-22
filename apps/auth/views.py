from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def authentication_view(request):
    #return HttpResponse("Bienvenue page accueil !")
    return render(request, 'home/index.html')
