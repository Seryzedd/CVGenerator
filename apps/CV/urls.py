from django.urls import path
from apps.CV.views import CV_id_view

urlpatterns = [
    path('', CV_id_view, name='cvNew')
]