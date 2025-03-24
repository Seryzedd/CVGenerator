from django.http import HttpResponse
from django.shortcuts import render, redirect
from apps.account.forms.login_form import LoginForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

class CustomLogin(LoginView):
    template_name = 'index.html'
    authentication_form = LoginForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def get_success_url(self):
        """
        Determine url de redirection apres connexion
        :return:
        """

        return self.success_url

    def form_valid(self, form):
        """
        Connexion et message de succès
        :param form:
        :return:
        """

        print(self.request)
        exit()
        messages.success(self.request, 'Connexion réussie.')
        return super().form_valid(form)

    def form_invalid(self, form):
        """ Connexion echoué et message d'alerte"""
        messages.error(self.request, "Identifiants invalides. Connexion échouée !")
        return super().form_invalid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
