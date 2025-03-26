from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.CV.forms.CVForm import CvForm

# Vue existante pour la création de CV
def CV_id_view(request):
    form = CvForm(request.POST or None)
    return render(request, 'CVNew/index.html', {'form': form})

# Page d'accueil
def home(request):
    return render(request, 'home.html')

# Page de contact
def contact(request):
    return render(request, 'contact.html')

# Page de gestion utilisateur (login, etc.)
@login_required
def user_management(request):
    return render(request, 'user_management.html')

# Page de gestion CV
@login_required
def cv_management(request):
    return render(request, 'cv_management.html')

# Génération de CV
@login_required
def cv_generate(request):
    return render(request, 'cv_generate.html')
