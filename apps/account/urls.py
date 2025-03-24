from django.urls import path
from apps.account.views import CustomLogin

urlpatterns = [
    path('login/', CustomLogin.as_view(), name='login')
]