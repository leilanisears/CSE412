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
    path('delete/<slug:the_slug>/', PlaylistDeleteView.as_view(), name='playlist-delete'),
    path('playlistbuilder/', PlaylistSelectView.as_view(), name='my-playlists'),
    path('playlistbuilder/<slug:the_slug>/', PlaylistBuildView.as_view(), name='build-playlist'),
]

