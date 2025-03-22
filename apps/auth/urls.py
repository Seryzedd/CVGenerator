from django.urls import path
from apps.auth.views import authentication_view

urlpatterns = [
    path('', authentication_view, name='auth')
]