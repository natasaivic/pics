from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("registration/", views.registration),
    path("login/", views.login),
    path("profile/", views.profile),
    path("feed/", views.feed),
]