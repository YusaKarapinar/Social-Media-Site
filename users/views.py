from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required

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
    return redirect('users/login')

from django.shortcuts import render


# Profil Sayfası Görünümü
@login_required(login_url='/login/')
def profile_page(request, username):
    user = get_object_or_404(CustomUser, username=username)
    context = {
        "user_profile": user
    }
    return render(request, 'profile/profile.html', context)

# Kullanıcı Arama
@login_required(login_url='/login/')
def search_user(request):
    query = request.GET.get('query', '')
    results = CustomUser.objects.filter(username__icontains=query)
    return render(request, 'profile/search_results.html', {'results': results})