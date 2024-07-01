from django.shortcuts import render
from .models import *
from django.contrib.auth import logout


def index(request):
    return render(request, 'social/index.html')


def log_out(request):
    logout(request)
    return render(request, 'registration/logged_out.html')
