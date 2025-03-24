from django.urls import path
from apps.login.views import customLoginView

urlpatterns = [
    path('', customLoginView.as_view(), name='login')
]