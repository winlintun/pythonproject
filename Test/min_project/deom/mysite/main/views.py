from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import Tutorial
from django.contrib import messages
from .form import NewUserForm


def homepage(request):
    tutorials = Tutorial.objects.all
    return render(request, 'main/home.html', {'tutorials': tutorials})


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error (f"{msg}: {form.error_messages[msg]}")
    form = NewUserForm
    return render(request, 'main/register.html', {"form": form})


def logout_request(request):
    logout(request)
    messages.success(request, f"Logout Successful")
    return redirect("main:homepage")


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Login Successful")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username and password")
        else:
            messages.error(request, "Invalid username and password")

    form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})