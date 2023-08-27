from django.shortcuts import render

def login(request):
    return render(request, 'login.html')


def signUp(request):
    return render(request, 'signUp.html')


def home(request):
    return render(request, 'home.html')