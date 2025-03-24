from django.urls import path
from apps.login.views import customLoginView, registerAccount

urlpatterns = [
    path('login/', customLoginView.as_view(), name='login'),
    path('register/', registerAccount, name='register')
]