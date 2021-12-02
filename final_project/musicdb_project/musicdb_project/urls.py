"""musicdb_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from users import views as user_views
from musicdb import views as music_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('welcome/', include("musicdb.urls")),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # If I have time to revamp users, I will be adding user views here
    path('register/', user_views.register, name='register'),
    path('u/', user_views.profile, name='user-profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('create/', music_views.PlaylistCreateView.as_view(template_name='playlist_create.html'), name='playlist-create'),
    path("u/<str:username>/playlists", music_views.UserPlaylistView.as_view(), name="user-playlists"),
    #path('u/', include("users.urls")),
    path('contact/', include("contact.urls")),
    #path('search/', include("search.urls")),
    path('', include('musicdb.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
