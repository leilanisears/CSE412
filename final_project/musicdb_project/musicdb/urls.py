from django.urls import path
from . import views

urlpatterns = [
    path("search/", views.search, name="search"),
    path("create/(?P<user_id>\d+)/", views.create_playlist, name="create playlist"),
    path("add_remove/(?P<user_id>\d+)/(?P<playlist_id>d+)/(r'^[a-zA-Z]')/", views.add_remove_songs, name="add or remove songs from playlist"),
    path("editplaylist/(?P<user_id<\d+)/(?P(<playlist_id>\d+)/)(r'^[a-zA-Z]')/", views.edit_playlist, name="edit playlist name or delete")

