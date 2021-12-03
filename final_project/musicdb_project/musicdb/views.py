from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from musicdb.models import Playlist, Song
from users.models import User

from django.forms import ModelForm
from .forms import PlaylistForm

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.http import Http404, JsonResponse, HttpResponseForbidden, HttpResponse

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from . import clientAPI
import string, random, json

#####################################################################


def about(request):
    return render(request, "about.html", {'title': 'About'})
class PlaylistView(ListView):
    model = Playlist
    template_name = 'home.html'
    context_object_name = 'playlists'
    ordering = ['-date_updated']
    slug_url_kwarg = 'the_slug'
    slug_field = 'slug'
class UserPlaylistView(ListView):
    model = Playlist
    template_name = 'user_profile.html'
    context_object_name = 'playlists'
    ordering = ['-date_updated']
    slug_url_kwarg = 'the_slug'
    slug_field = 'playlist_id'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Playlist.objects.filter(creator=user).order_by("-date_created")
class PlaylistDetailView(DetailView):
    model = Playlist
    template_name = 'playlist_detail.html'
    context_object_name = 'playlist'
    slug_url_kwarg = 'the_slug'
    slug_field = 'playlist_id'

class SearchPlaylistView(ListView):
    model = Playlist
    template_name = 'search_playlists.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = set(Playlist.objects.filter(Q(playlist_name__icontains=query)))
        return object_list

class SearchSongView(ListView):
    model = Song
    template_name = 'search_songs.html'
    context_object_name = 'songs'

    def get_queryset(self):
        query = self.request.GET.get('q')

        songs = None

        if query:
            songs = set(Song.objects.filter(
                Q(song_name__icontains=query) |
                Q(song_artists__icontains=query)
            ))
            if len(songs) == 0:
                client = clientAPI.APICall()

                spotify_song = client.get_song(query)

                artists = spotify_song.get("artists")

                s = Song()
                s.song_id = spotify_song.get("id")
                s.song_artists = ', '.join(artists)
                s.song_name = spotify_song.get("name")
                s.song_link = spotify_song.get("link")
                s.save()

                songs = set(Song.objects.filter(
                    Q(song_name__icontains=query) |
                    Q(song_artists__icontains=query)
                ))

        return songs

class PlaylistCreateView(LoginRequiredMixin, CreateView):
    model = Playlist
    fields = ('playlist_name', 'playlist_link')
    template_name = 'playlist_create.html'
    slug_url_kwarg = 'the_slug'
    slug_field = 'playlist_id'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class PlaylistUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Playlist
    fields = ('playlist_name',)
    template_name = 'playlist_update.html'
    slug_url_kwarg = 'the_slug'
    slug_field = 'playlist_id'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def test_func(self):
        playlist = self.get_object()
        if self.request.user == playlist.creator:
            return True
        return False

class PlaylistDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Playlist
    success_url = '/'
    context_object_name = 'playlist'
    template_name = 'playlist_confirm_delete.html'
    slug_url_kwarg = 'the_slug'
    slug_field = 'playlist_id'

    def test_func(self):
        playlist = self.get_object()
        if self.request.user == playlist.creator:
            return True
        return False

class PlaylistSelectView(LoginRequiredMixin, ListView):
    model = Playlist
    context_object_name = 'playlists'
    template_name = 'playlist_select.html'
    ordering = ['-date_updated']
    slug_url_kwarg = 'the_slug'
    slug_field = 'playlist_id'

class PlaylistBuildView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Playlist
    fields = ('playlist_name', 'playlist_link', 'songs',)
    context_object_name = 'playlists'
    template_name = 'playlist_build.html'
    slug_url_kwarg = 'the_slug'
    slug_field = 'playlist_id'

    def form_valid(self, form):
        playlist = self.get_object()
        song = form.cleaned_data['songs']

        playlist.save()

        song_list = Song.objects.filter(pk__in=song)
        for song in song_list:
            playlist.songs.add(song)
        
        return super().form_valid(form)

    def test_func(self):
        playlist = self.get_object()
        if self.request.user == playlist.creator:
            return True
        return False
    


# generates a randomized string for the playlist_id (primary key) to be indexed
# def generate_playlist_id():
#     letters = string.ascii_letters
#     letters += string.digits

#     return ''.join(random.choice(letters) for i in range(20))

# def display_all_playlists(request, user_id):
#     user = get_object_or_404(UserEntity, id=user_id)
#     all_playlists = user.playlists.all()

#     data = {
#         'user': user,
#         'playlists': all_playlists
#     }

#     return(render, 'display_all.html', data)

# def create_playlist(request, user_id):
#     user = get_object_or_404(UserEntity, id=user_id)

#     if request.user != user:
#         return HttpResponseForbidden()

#     if request.method == "POST":
#         form = PlaylistForm(request.POST)

#         if form.is_valid():
#             form = PlaylistForm(request.POST)

#             playlist = form.save(commit=False)
#             #playlist.playlist_id = generate_playlist_id()
#             playlist.save()

#             user.playlists.add(playlist)

#             return redirect('playlists.html', request)

# def add_remove_songs(request, user_id):
#     user = get_object_or_404(UserEntity, id=user_id)

#     playlist_id = request.data.get('playlist_id')
#     playlist = get_object_or_404(Playlist, id=playlist_id)

#     req_type = request.data.get('type')

#     if request.method == "POST":

#         songs = Song.objects.all()

#         if req_type == "add":
#             #songs = Song.objects.all()

#             selected_song_id = request.data.get('track_id')
#             selected_song = Song.object.get(id=selected_song_id)

#             playlist.songs.add(selected_song)

#         elif req_type == "remove":
#             selected_song_id = request.data.get('track_id')
#             selected_song = Song.object.get(id=selected_song_id)

#             playlist.songs.remove(selected_song)


#         return render(request, 'add_remove_songs.html', {'songs':songs})

#     return redirect('display_playlists', request)

# def edit_playlist(request, user_id):
#     user = get_object_or_404(UserEntity, id=user_id)

#     playlist_id = request.data.get('playlist_id')
#     playlist = get_object_or_404(Playlist, id=playlist_id)

#     req_type = request.data.get('type')

#     #playlists = Playlist.objects.all()

#     if request.method == "POST":
#         if req_type == "edit":
#             form = PlaylistForm(request.POST, instance=playlist)

#             if form.is_valid():
#                 form.save()

#         elif req_type == "delete":
#             user.playlists.remove(playlist)

#         return redirect("display_all_playlists", request)
