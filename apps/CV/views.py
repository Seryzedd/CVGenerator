from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, redirect
from apps.CV.forms.CVForm import CvForm
from apps.CV.models.CV import CV

def CV_id_view(request):
    if not request.user.is_authenticated:
        messages.info(request, "You need to login to create CV.")
        return redirect('login')
    form = CvForm(request.POST or None)
    if form.is_valid():
        try:
            cleaned_data = form.clean()

            new_cv = CV()
            new_cv.object.createNew(
                name=cleaned_data['name'],
                description=cleaned_data['description'],
                template=cleaned_data['template'],
                primaryColor=cleaned_data['primaryColor'],
                secondaryColor=cleaned_data['secondaryColor'],
                user=request.user
            )

            messages.success(request, "CV créé !")

            messages.info(request, "Vous pouvez completer la configuration du CV.")

            return redirect('home')
        except IntegrityError:
            messages.error(request, 'Erreur lors de la génération du CV.')
        except Exception as e:
            messages.error(request, f"Une erreur est survenue : {e}")

    return render(request, 'CVNew/index.html', {'form': form})