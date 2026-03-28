from django.contrib.auth.views import LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserRegistrationForm


class SignupView(CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class CustomLogoutView(LogoutView):
    http_method_names = ['post']
    next_page = reverse_lazy('login')
    template_name = 'registration/logout.html'
    success_url = reverse_lazy('login')
