from django.urls import path, re_path
from .views import (
    PlaylistView,
    PlaylistDetailView,
    PlaylistUpdateView,
    PlaylistCreateView,
    PlaylistDeleteView,
    PlaylistSelectView,
    PlaylistBuildView,
    SearchPlaylistView,
    SearchSongView,
)
from . import views

urlpatterns = [
    path('', PlaylistView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('search/songs/', SearchSongView.as_view(), name='search-songs'),
    path('search/playlists/', SearchPlaylistView.as_view(), name='search-playlists'),
    path('playlist/<slug:the_slug>/', PlaylistDetailView.as_view(), name='playlist-detail'),
    path('update/update?p=<playlist_id>/', PlaylistUpdateView.as_view(), name='playlist-update'),
    path('delete/delete?p=<playlist_id>/', PlaylistDeleteView.as_view(), name='playlist-delete'),
    path('playlistbuilder/', PlaylistSelectView.as_view(), name='my-playlists'),
    path('playlistbuilder/<slug:the_slug>/', PlaylistBuildView.as_view(), name='build-playlist'),

    # path("addremove/<str:user_id>/<slug:playlist_id>/<str:action>", views.add_remove_songs, name="add or remove songs from playlist"),
    # path("editplaylist/<str:user_id>/<slug:playlist_id>/<str:action>/", views.edit_playlist, name="edit playlist name or delete playlist"),
]

