from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import SignupView, custom_logout

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path("accounts/logout/", custom_logout, name="logout"),
]