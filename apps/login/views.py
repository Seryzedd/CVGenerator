from django.contrib.auth.views import LoginView, LogoutView
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from apps.login.forms.adress_form import AdressForm
from apps.login.forms.login_form import LoginForm
from apps.login.models import User, Adress
from django.contrib import messages
from apps.login.forms.register_form import RegisterForm

# Create your views here.
class CustomLoginView(LoginView):
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

def registerAccount(request) :
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        # Traitement si le formulaire est valide
        cleaned_data = form.cleaned_data
        try:

            User.objects.create_user(
                username=cleaned_data['username'],
                email=cleaned_data['email'],
                firstname=cleaned_data['firstname'],
                lastname=cleaned_data['lastname'],
                password=cleaned_data['password']
            )

            messages.success(request, "Inscription réussie !")

            return redirect('login')
        except IntegrityError:
            messages.error(request, 'Email déjà utilisé.')
        except Exception as e:
            print(e)
            messages.error(request, f"Une erreur est survenue : {e}")

    return render(request, 'register.html', {
        'form': form
    })

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, 'Vous avez été déconnecté !')

        return super().dispatch(request, *args, **kwargs)

def addressView(request):
    form = AdressForm(request.POST or None)

    if request.user.adress:
        form.setData(request.user)

    if form.is_valid():
        # Traitement si le formulaire est valide
        cleaned_data = form.cleaned_data
        try:
            adress = Adress()
            adress.update(
                cleaned_data
            )

            request.user.adress=adress
            request.user.save()
            # User.objects.create_user(
            #     username=cleaned_data['username'],
            #     email=cleaned_data['email'],
            #     firstname=cleaned_data['firstname'],
            #     lastname=cleaned_data['lastname'],
            #     password=cleaned_data['password']
            # )

            messages.success(request, "Address enregistré !")

            return redirect('home')
        except Exception as e:
            print(e)
            messages.error(request, f"Une erreur est survenue : {e}")
    return render(request, 'adress.html', {
        'form': form
    })