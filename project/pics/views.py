from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

from django.contrib import messages

from .models import *
from .forms import PicsUserForm
 
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return HttpResponse("The project aims to develop an Instagram-like app using Python, Django, PostgreSQL, Django REST Framework, HTML/CSS, React, and Bootstrap.")


# The initial step in creating a new account on the platform. With this method, new users can sign up and provide the necessary information to create their Pics account. 
def registration(request):
    if request.method == "POST":
        form = PicsUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account has been successfully registered. ")
            return redirect('login_page')  
        else:
            print(f"Error: {form.errors}")
    else:
        form = PicsUserForm()
    context = {'form':form}
    return render(request, 'pics/registration.html', context)


# This method renders the page that appears after the registration process, or when users log out and want to log back in to their account. 
# Login view handles the login form submission.
def login_page(request):
    if request.method == "POST":
        print("First step is done! ")
        username = request.POST.get('username')
        print(f"Username: {username}")
        print("Username is obtained! ")
        password = request.POST.get('password')
        print(f"Password: {password}")
        print("Password is obtained! ")
        user = authenticate(request, username=username, password=password)
        print("Authentication completed! ")
        print(user)
        if user is not None:
            # A backend authenticated the credentials
            pass
        else:
            print("'Username or password is incorrect! ")
            messages.info(request, 'Username or password is incorrect.')
            
    context = {}
    return render(request, 'pics/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login_page')

# This method renders the profile page displays a grid of images as a visual representation of the user's posts.
# @login_required(login_url='login_page')
def profile(request):
    # user = request.user
    # username = user.username
    # name = user.name
    # bio = user.bio
    # posts = Post.objects.filter(user=user)
    # context = {'user':user, 'username':username, 'name':name, 'bio':bio, 'posts':posts}
    return render(request, 'pics/profile.html')


def edit_profile_pic(request):
    return HttpResponse("Profile picture upload. ")


# The news feed displays photos shared by the accounts that the user follows.
@login_required(login_url='login_page')
def feed(request):
    return render(request, 'pics/feed.html')