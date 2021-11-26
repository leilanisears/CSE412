from django.shortcuts import render, redirect, get_object_or_404
from musicdb.models import Playlist, Song

from django.forms import ModelForm
from .forms import RequestForm, PlaylistCreateForm

from django.http import Http404, JsonResponse, HttpResponseForbidden


################################################################################


# generate playlist_ids
def generate_id():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(25))

def form_data(user, form):
    data = {
        'owner': user,
        'playlist_form': form,
    }

    return data

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

def request_success(request):
    context = {}
    return render(request, "request_success.html", context)

def song_request(request):
    context = {}
    if request.method == "POST":
        #context = {}

        form = RequestForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('request_success')

        context['form'] = form
        #return redirect()

    return render(request, "songrequest.html", context)

def display_all(request, user_id):
    user = get_object_or_404(UserEntity, id=user_id)

    if request.user != user:
        return HttpResponseForbidden()

    playlists = Playlist.objects.get(owner_name=user.display_name)

    if request.method == "GET":
        data = {
            'owner': user,
            'playlists': playlists
        }

        return render(request, 'display_all.html', data)

def display_playlists(request, user_id, playlist_id):
    user = get_object_or_404(UserEntity, id=user_id)

    if request.user != user:
        return HttpResponseForbidden()

    playlist = get_object_or_404(Playlist, id=playlist_id, user=user)
    if request.method == "GET":
        data = {
            'owner': user,
            'playlist': playlist,
        }

        return render(request, 'display_playlist.html', data)

def create_playlist(request, userid):
    user = get_object_or_404(UserEntity, id=user_id)
    if request.user != user:
        return redirect('create_playlist', request.user_id)

    if request.method == "POST":
        form = PlaylistCreateForm(request.POST)

        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.owner_name = request.user
            playlist.playlist_id = generate_ids()
            playlist.date_created = models.DateTimeField(default=datetime.now, blank=True)
            playlist.save()

            return redirect('display_playlists', request.user_id)

    return render(request, 'create_form.html', data)

def edit_playlist(request, user_id, playlist_id):
    user = get_object_or_404(UserEntity, id=user_id)
    playlist = get_object_or_404(Playlist, id=playlist_id, user=user)

    if request.user != user:
        return redirect('create_playlist', request.user_id)
    if request.playlist != playlist:
        return redirect('playlist_not_found')

    form = PlaylistCreateForm(request.POST, instance=playlist)

    if form.is_valid():
        playlist = form.save()

        return redirect('display_playlists', request.user_id)

    return render('create_playlist', request.user_id)

def delete(request, user_id, playlist_id):
    user = get_object_or_404(UserEntity, id=user_id)
    playlist = get_object_or_404(Playlist, id=playlist_id, user=user)

    if request.user != playlist.user:
        return HttpResponseForbidden()

    playlist.delete()

    return redirect('display_playlists', user_id)
