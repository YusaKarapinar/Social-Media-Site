from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import RegisterForm, LoginForm

# Kayıt Sayfası
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

# Giriş Sayfası
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

# Çıkış İşlemi
def logout_view(request):
    logout(request)
    return redirect('home')

from django.shortcuts import render

# Ana Sayfa Görünümü
def home_view(request):
    return render(request, 'home.html')
