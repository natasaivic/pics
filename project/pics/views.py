from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("The project aims to develop an Instagram-like app using Python, Django, PostgreSQL, Django REST Framework, HTML/CSS, React, and Bootstrap.")


def registration(request):
    return HttpResponse("Here is the initial step in creating a new account on the platform. It is the page where new users can sign up and provide the necessary information to create their Pics account. ")


def login(request):
    return HttpResponse("This is the page that appears after the registration process, or when users log out and want to log back in to their account. ")


def profile(request):
    return HttpResponse("The profile page displays a grid of images as a visual representation of the user's posts.")


def feed(request):
    return HttpResponse("The news feed displays photos shared by the accounts that the user follows.")