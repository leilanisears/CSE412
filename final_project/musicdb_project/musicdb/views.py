from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from musicdb.models import Playlist, Song
from users.models import UserEntity

from django.forms import ModelForm
from .forms import PlaylistForm

from django.http import Http404, JsonResponse, HttpResponseForbidden

import .apirequests
import string, random

#####################################################################

class SearchView(ListView):
    model = Song
    template_name = 'search.html'
    context_name = 'all_results'

    def get_queryset(self):
        result = super(SearchView, self). get_queryset()
        query = self.request.GET.get('search')

        song = None

        if query:
            try:
                songs = Song.objects.filter(
                    Q(track_name__icontains=query) |
                    Q(artist_name__icontains=query)
                )
            except Song.DoesNotExist:
                client = apirequests.APICall()
                #token = client.get_access_token()

                songs = json.load(client.get_song(token, query))

                for s in songs:
                    new_song = Song()

                    new_song.song_id = s.get("id")
                    new_song.song_artists = s.get("artists")
                    new_song.song_name = s.get("name")
                    new_song.song_link = s.get("link")

                    s.save()

                songs = Song.objects.filter(
                    Q(track_name__icontains=query) |
                    Q(artist_name__icontains=query)
                )

                pass

# generates a randomized string for the playlist_id (primary key) to be indexed
def generate_playlist_id():
    letters = string.ascii_letters
    letters += string.digits

    return ''.join(random.choice(letters) for i in range(20))

def display_all_playlists(request, user_id):
    user = get_object_or_404(UserEntity, id=user_id)
    all_playlists = user.playlists.all()

    data = {
        'user': user,
        'playlists': all_playlists
    }

    return(render, 'display_all.html', data)

def create_playlist(request, user_id):
    user = get_object_or_404(UserEntity, id=user_id)

    if request.user != user:
        return HttpResponseForbidden()

    if request.method == "POST":
        form = PlaylistForm(request.POST)

        if form.is_valid():
            form = PlaylistForm(request.POST)

            playlist = form.save(commit=False)
            playlist.playlist_id = generate_playlist_id()
            playlist.save()

            user.playlists.add(playlist)

            return redirect('playlists.html', request)

def add_remove_songs(request, user_id):
    user = get_object_or_404(UserEntity, id=user_id)

    playlist_id = request.data.get('playlist_id')
    playlist = get_object_or_404(Playlist, id=playlist_id)

    req_type = request.data.get('type')

    if request.method == "POST":

        songs = Song.objects.all()

        if req_type == "add":
            #songs = Song.objects.all()

            selected_song_id = request.data.get('track_id')
            selected_song = Song.object.get(id=selected_song_id)

            playlist.songs.add(selected_song)

        elif req_type == "remove":
            selected_song_id = request.data.get('track_id')
            selected_song = Song.object.get(id=selected_song_id)

            playlist.songs.remove(selected_song)


        return render(request, 'add_remove_songs.html', {'songs':songs})

    return redirect('display_playlists', request)

def edit_playlist(request, user_id):
    user = get_object_or_404(UserEntity, id=user_id)

    playlist_id = request.data.get('playlist_id')
    playlist = get_object_or_404(Playlist, id=playlist_id)

    req_type = request.data.get('type')

    #playlists = Playlist.objects.all()

    if request.method == "POST":
        if req_type == "edit":
            form = PlaylistForm(request.POST, instance=playlist)

            if form.is_valid():
                form.save()

        elif req_type == "delete":
            user.playlists.remove(playlist)

        return redirect("display_all_playlists", request)
