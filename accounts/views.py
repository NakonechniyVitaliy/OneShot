from django.shortcuts import render, redirect
from orders.models import Order
from accounts.forms import RegisterUserForm, AuthenticationUserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def sign_up(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'accounts/reports.html')
    else:
        form = RegisterUserForm()
    return render(request, 'accounts/sign_up.html', {'form': form})


def sign_in(request):
    if request.method == 'POST':
        form_2 = AuthenticationUserForm(data=request.POST)
        if form_2.is_valid():
            user = form_2.get_user()
            login(request, user)
            return redirect('/')
    else:
        form_2 = AuthenticationUserForm()
    return render(request, 'accounts/sign_in.html', {'form_2': form_2})


def sign_out(request):
    logout(request)
    return redirect('/')


def profile(request):
    return render(request, 'accounts/profile.html', context={
        'title': 'Профіль користувача',
        'app': 'Profile',
    })



