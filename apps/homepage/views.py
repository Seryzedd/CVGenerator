from django.shortcuts import render, redirect
from apps.CV.models.CV import CV
from django.contrib import messages


def homepage_view(request):

    if request.user.is_authenticated:
        CVs = CV.object.getByUser(request.user)
    else:
        messages.info(request, 'Login first to use CV Generator.')
        return redirect('login')
    return render(request, 'homepage/index.html', {'cvs': CVs})