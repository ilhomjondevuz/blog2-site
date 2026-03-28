from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserRegistrationForm


class SignupView(CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def custom_logout(request):
    logout(request)
    return redirect("login")  # yoki bosh sahifa
