from django.urls import path, re_path
from .views import (
    PlaylistView,
    PlaylistDetailView,
    PlaylistCreateView,
    PlaylistUpdateView,
    PlaylistCreateView,
    PlaylistDeleteView,
    UserPlaylistView,
    SearchPlaylistView,
    SearchSongView,
)
from . import views

urlpatterns = [
    path('', PlaylistView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('search/songs', SearchSongView.as_view(), name='search-songs'),
    path('search/playlists', SearchPlaylistView.as_view(), name='search-playlists'),
    path('playlist/<slug:playlist_id>/', PlaylistDetailView.as_view(), name='playlist-detail'),
    path("<str:user_id>/playlists", UserPlaylistView.as_view(), name="user-playlists"),
    path('create/', PlaylistCreateView.as_view(), name='playlist-create'),
    path('update/update?p=<playlist_id>/', PlaylistUpdateView.as_view(), name='playlist-update'),
    path('delete/delete?p=<playlist_id>/', PlaylistDeleteView.as_view(), name='playlist-delete'),

    # path("addremove/<str:user_id>/<slug:playlist_id>/<str:action>", views.add_remove_songs, name="add or remove songs from playlist"),
    # path("editplaylist/<str:user_id>/<slug:playlist_id>/<str:action>/", views.edit_playlist, name="edit playlist name or delete playlist"),
]

