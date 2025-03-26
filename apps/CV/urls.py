from django.urls import path
from apps.CV.views import CV_id_view, CVManageExistingCV

urlpatterns = [
    path('', CV_id_view, name='cvNew'),
    path("<str:name>", CVManageExistingCV, name='cvUpdate')
]