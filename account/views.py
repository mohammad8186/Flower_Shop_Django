from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from account.forms import LoginForm

from account.forms import RegisterForm


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('login-register')
  

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)
                return redirect('product_list')
    return redirect('login-register')
  
  
def login_register(request):
    return render(request , "account/login-register.html")


def logout_view(request):
    logout(request)
    return redirect('login-register')

