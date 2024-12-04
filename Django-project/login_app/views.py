import requests
from django.shortcuts import render
from django.http import JsonResponse

def login_view(request):
    return render(request, 'login.html')

def main_view(request):
    return render(request, 'main.html')

def profile_view(request):
    return render(request, 'profile.html')

def register_view(request):
    return render(request, 'register.html')