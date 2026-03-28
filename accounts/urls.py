from django.urls import path

from .views import SignupView, CustomLogoutView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]