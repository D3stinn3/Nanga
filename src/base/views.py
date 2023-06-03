from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
# Create your views here.
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


def profile_page(request):
    context = {}
    
    return render(request, 'index.html', context)

def signup_page(request):
    context = {}
    
    return render(request, 'signup.html', context)

@login_required(login_url='/login')
def account_page(request, pk):
    user = request.user
    context = {'user' : user} 
    return render(request, 'account.html', context)