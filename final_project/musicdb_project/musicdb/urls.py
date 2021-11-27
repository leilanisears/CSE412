from django.urls import path
from . import views

urlpatterns = [
    path("songrequest/", views.song_request, name="song request"),
    path("<user_id>/<playlist_id>/", views.display_playlists, name="playlist view"),
    path("create/", views.create_playlist, name="create playlist"),
    path("<playlist_id>/edit/", views.edit_playlist, name="edit playlist"),
    path("<user_id>/<playlist_id>/delete/", views.delete, name="delete playlist"),

]
