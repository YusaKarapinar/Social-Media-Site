from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from posts.models import Post, Comment
from .forms import EditProfileForm
# Kayıt Sayfası
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('feed_page')
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
    user_profile = get_object_or_404(CustomUser, username=username)
    posts = Post.objects.filter(author=user_profile)
    comments = Comment.objects.filter(author=user_profile)
    followers_count = user_profile.followers.count()
    following_count = user_profile.following.count()

    context = {
        'user_profile': user_profile,
        'posts': posts,
        'comments': comments,
        'followers_count': followers_count,
        'following_count': following_count,
    }
    return render(request, 'profile/profile.html', context)

# Kullanıcı Arama
@login_required(login_url='/login/')
def search_user(request):
    query = request.GET.get('query', '')
    results = CustomUser.objects.filter(username__icontains=query)
    return render(request, 'profile/search_results.html', {'results': results})



@login_required(login_url='/login/')
def follow_user(request, username):
    user_to_follow = get_object_or_404(CustomUser, username=username)
    if request.user.is_authenticated:
        user_to_follow.followers.add(request.user)
    return redirect('profile_page', username=username)

@login_required(login_url='/login/')
def unfollow_user(request, username):
    user_to_unfollow = get_object_or_404(CustomUser, username=username)
    if request.user.is_authenticated:
        user_to_unfollow.followers.remove(request.user)
    return redirect('profile_page', username=username)



@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile_page', username=request.user.username)
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'profile/edit_profile.html', {'form': form})
