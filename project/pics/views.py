from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("The project aims to develop an Instagram-like app using Python, Django, PostgreSQL, Django REST Framework, HTML/CSS, React, and Bootstrap.")


# The initial step in creating a new account on the platform. With this method, new users can sign up and provide the necessary information to create their Pics account. 
def registration(request):
    return render(request, 'pics/registration.html')


# This method renders the page that appears after the registration process, or when users log out and want to log back in to their account. 
def login(request):
    return render(request, 'pics/login.html')


# This method renders the profile page displays a grid of images as a visual representation of the user's posts.
def profile(request):
    return render(request, 'pics/profile.html')


# The news feed displays photos shared by the accounts that the user follows.
def feed(request):
    return render(request, 'pics/feed.html')