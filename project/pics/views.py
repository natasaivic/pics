from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

from .models import *
from .forms import PicsUserForm

# Create your views here.
def index(request):
    return HttpResponse("The project aims to develop an Instagram-like app using Python, Django, PostgreSQL, Django REST Framework, HTML/CSS, React, and Bootstrap.")


# The initial step in creating a new account on the platform. With this method, new users can sign up and provide the necessary information to create their Pics account. 
def registration(request):
    if request.method == "POST":
        form = PicsUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
        else:
            form.add_error(None, 'The form is not valid.')
            form = PicsUserForm()
    form = PicsUserForm()
    context = {'form':form}
    return render(request, 'pics/registration.html', context)


# This method renders the page that appears after the registration process, or when users log out and want to log back in to their account. 
# Login view handles the login form submission.
def login(request):
    form = PicsUserForm()
    return render(request, 'pics/login.html', {'form': form})


def logout(request):
    return render(request, 'pics/logout.html')

# This method renders the profile page displays a grid of images as a visual representation of the user's posts.
def profile(request):
    user = request.user
    username = user.username
    name = user.name
    bio = user.bio
    posts = Post.objects.filter(user=user)
    context = {'user':user, 'username':username, 'name':name, 'bio':bio, 'posts':posts}
    return render(request, 'pics/profile.html', context)


# The news feed displays photos shared by the accounts that the user follows.
def feed(request):
    return render(request, 'pics/feed.html')