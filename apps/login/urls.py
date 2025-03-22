from django.urls import path
from apps.login.views import login_view

urlpatterns = [
    path('', login_view, name='login')
]