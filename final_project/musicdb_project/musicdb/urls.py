from django.urls import path
from . import views

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("<int:pk>/", views.playlist_detail, name="playlist detail"),
]