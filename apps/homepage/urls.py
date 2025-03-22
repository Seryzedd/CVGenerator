from django.urls import path
from apps.homepage.views import homepage_view

urlpatterns = [
    path('', homepage_view, name='home')
]