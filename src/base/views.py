from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreate
# Create your views here.
# This is the login authenticator view
def login_page(request):
    
    if request.method == "POST":
        username = authenticate(
            email=request.POST['email'],
            password=request.POST['password']
            )
        
        if username is not None:
            login(request, username)
            return redirect('profile')
        
    context = {}
    
    return render(request, 'login.html', context)

def logout_page(request):
    logout(request)
    return redirect('home')


def profile_page(request):
    context = {}
    
    return render(request, 'index.html', context)

#This becomes the signin view
def signup_page(request):
    
    if request.method == "POST":
        form = UserCreate(request.POST)
        
        if form.is_valid():
            user = form.save()
            # username = form.cleaned_data.get('email')
            login(request, user)
            return redirect('login')
    else:
        form = UserCreate()
            
    context = {'form': form}
    
    return render(request, 'signup.html', context)

def landing_page(request):
    context = {}
    
    return render(request, 'landing.html', context)

@login_required(login_url='/login')
def account_page(request, pk):
    user = request.user
    context = {'user' : user} 
    return render(request, 'account.html', context)