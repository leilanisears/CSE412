from django.urls import path, re_path
from .views import (
    PlaylistView,
    # PlaylistDetailView,
    # PlaylistCreateView,
    # PlaylistUpdateView,
    SearchPlaylistView,
    SearchSongView,
    create_playlist,
    add_remove_songs,
    edit_playlist,

    
)
from . import views

urlpatterns = [
    path('', views.PlaylistView.as_view(), name='home'),
    path('search/', views.SearchSongView.as_view(), name='search'),
    path('playlist/<slug:playlist_id>/', views.PlaylistDetailView.as_view(), name='playlist-detail'),
    # path('create/', views.PlaylistCreateView, name='playlist-create'),
    # path('update/update?p=<playlist_id>/', views.PlaylistUpdateView, name='playlist-update'),
    path('about/', views.about, name='about'),
    path("create/<str:user_id>/", views.create_playlist, name="create playlist"),
    path("addremove/<str:user_id>/<str:playlist_id>/<str:action>", views.add_remove_songs, name="add or remove songs from playlist"),
    path("editplaylist/<str:user_id>/<str:playlist_id>/<str:action>/", views.edit_playlist, name="edit playlist name or delete playlist"),
]

