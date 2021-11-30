from django.urls import path, re_path
from . import views

urlpatterns = [
    path("search/", views.SearchView.as_view(), name="search"),
    path("create/<str:user_id>/", views.create_playlist, name="create playlist"),
    path("addremove/<str:user_id>/<str:playlist_id>/<str:action>", views.add_remove_songs, name="add or remove songs from playlist"),
    path("editplaylist/<str:user_id>/<str:playlist_id>/<str:action>/", views.edit_playlist, name="edit playlist name or delete playlist"),
]

