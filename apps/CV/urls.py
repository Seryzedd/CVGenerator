from django.urls import path
from apps.CV.views import CV_id_view, CVManageExistingCV, CVTemplateView, generatePDF

urlpatterns = [
    path('', CV_id_view, name='cvNew'),
    path("<str:name>", CVManageExistingCV, name='cvUpdate'),
    path("view/<int:id>", CVTemplateView, name='cvTemplateRender'),
    path("generate/<int:id>", generatePDF, name='generateCVPDF')
]