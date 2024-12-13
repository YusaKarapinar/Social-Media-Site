# main/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from posts.views import feed_page, delete_post , like_post ,post_detail 
from users.views import edit_profile, follow_user, profile_page ,search_user, unfollow_user
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', feed_page, name='feed_page'),  # Ana yol eklendi
    path('feed/', feed_page, name='feed_page'),
    path('messages/', views.messages_page, name='messages_page'),
    path('notifications/', views.notifications_page, name='notifications_page'),
    path('settings/', views.settings_page, name='settings_page'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),


    #post kısmı
    path('delete_post/<int:post_id>/', delete_post, name='delete_post'),
    path('like_post/<int:post_id>/', like_post, name='like_post'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),

    #profil kısmı
    path('profile/@<str:username>/', profile_page, name='profile_page'),
    path('search/', search_user, name='search_user'),
    path('edit/', edit_profile, name='edit_profile'),


    #folow
      path('<str:username>/follow/', follow_user, name='follow_user'),
    path('<str:username>/unfollow/', unfollow_user, name='unfollow_user'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)