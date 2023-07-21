from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import CustomAuthForm


urlpatterns = [
    path("", views.login_page),
    path("registration/", views.registration, name="registration"),
    path("login_page/", views.login_page, name="login_page"),
    path("profile/", views.profile, name="profil"),
    path("edit_profile_pic/", views.edit_profile_pic, name="edit_profile_pic"),
    path("feed/", views.feed, name="feed"),
    path("logout_user/", views.logout_user, name="logout_user"),
]