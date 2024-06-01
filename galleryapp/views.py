from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms.register_form import RegisterForm

def index(request):
    return redirect(to='home')

# def login(request):
#     return render(request, 'login.html')

def home(request):
    data = [*range(0, 20)]

    context = {
        "data": data
    }
    return render(request, 'home.html', context=context)

@login_required
def posts(request):
    data = [*range(0, 30)]

    context = {
        "data": data
    }
    return render(request, 'posts.html', context=context)

@login_required
def exit(request):
    logout(request)
    return redirect(to='home')
    

def register(request):
    form = RegisterForm()

    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context=context)