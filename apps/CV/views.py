from django.shortcuts import render
from apps.CV.forms.CVForm import CvForm

def CV_id_view(request):
    form = CvForm(request.POST or None)
    return render(request, 'CVNew/index.html', {'form': form})