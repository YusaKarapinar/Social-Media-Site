# main/views.py (veya uygun uygulamanız)
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from .forms import CustomUserCreationForm
from posts.models import Post
from posts.forms import PostForm

@login_required(login_url='/login/')
def profile_page(request):
    return render(request, 'profile/profile.html')




@login_required(login_url='/login/')
def messages_page(request):
    return render(request, 'messages/messages.html')

@login_required(login_url='/login/')
def notifications_page(request):
    return render(request, 'notifications/notifications.html')

@login_required(login_url='/login/')
def settings_page(request):
    return render(request, 'settings/settings.html')



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Başarılı kayıt sonrası giriş sayfasına yönlendirme
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})