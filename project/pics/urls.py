from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import CustomAuthForm


urlpatterns = [
    path("", views.login),
    path("registration/", views.registration, name="registration"),
    path("login/", views.login, name="login"),
    path("profile/", views.profile, name="profil"),
    path("feed/", views.feed, name="feed"),
    path("logout/", views.logout, name="logout"),
]