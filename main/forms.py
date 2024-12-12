from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Özel kullanıcı modeliniz
        fields = ('username', 'email', 'password1', 'password2')  # Görünmesini istediğiniz alanlar
