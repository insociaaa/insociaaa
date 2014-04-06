from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def facebook(request):
    return render(request, 'facebook.html')

def google(request):
    return render(request, 'google.html')

def linkedin(request):
    return render(request, 'linkedin.html')

def twitter(request):
    return render(request, 'twitter.html')

def yahoo(request):
    return render(request, 'yahoo.html')
