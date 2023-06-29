from django.urls import path

from . import views

urlpatterns = [
    path("", views.login),
    path("registration/", views.registration),
    path("login/", views.login),
    path("profile/", views.profile),
    path("feed/", views.feed),
    path("logout/", views.logout),
]