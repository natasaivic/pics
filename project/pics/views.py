from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("The project aims to develop an Instagram-like app using Python, Django, PostgreSQL, Django REST Framework, HTML/CSS, React, and Bootstrap.")