from django.shortcuts import render
from .models import User

# Create your views here.
def login_page(request):
    context = {}
    
    return render(request, 'login.html', context)


def profile_page(request):
    context = {}
    
    return render(request, 'index.html', context)

def signup_page(request):
    context = {}
    
    return render(request, 'signup.html', context)

def account_page(request, pk):
    user = request.user
    context = {'user' : user} 
    return render(request, 'account.html', context)