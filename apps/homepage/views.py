from django.shortcuts import render
from apps.CV.models.CV import CV

# Create your views here.

def homepage_view(request):
    CVs = None
    if request.user.is_authenticated:
        CVs = CV.object.getByUser(request.user)
    return render(request, 'homepage/index.html', {'cvs': CVs})