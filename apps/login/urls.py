from django.urls import path
from apps.login.views import CustomLoginView, registerAccount, CustomLogoutView, addressView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('adress/', addressView, name='adress'),
    path('register/', registerAccount, name='register'),
    path('logout/', CustomLogoutView.as_view(), name='logout')
]