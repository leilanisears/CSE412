from django.shortcuts import render
from musicdb.models import Playlist, Song
from django.http import HTTPResponseRedirect
from django.shortcut import render

from django.forms import ModelForm

# Create your views here.

def playlist_detail(request, pk):
    playlist_obj = Playlist.objects.get(pk=pk)
    song_objs = Song.objects.filter(song_id=playlist_obj.song_id)
    context = {
        "playlists": playlist_obj,
        "songs": song_objs,
    }
    return render(request, "playlist_detail.html", context)

def welcome(request):
    context = {}
    return render(request, "welcome.html", context)

def db_request(request):
    if request.method == "POST":

