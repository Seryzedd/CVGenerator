from django.urls import path
from apps.CV.views import home, contact, user_management, cv_management, cv_generate, CV_id_view

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('user-management/', user_management, name='user_management'),
    path('cv-management/', cv_management, name='cv_management'),
    path('cv-generate/', cv_generate, name='cv_generate'),
    path('cv-id/', CV_id_view, name='cvNew'),  # Garder cette route existante
]
