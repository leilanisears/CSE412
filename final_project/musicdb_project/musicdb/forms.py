from django import forms
from .models import Song, Playlist

class RequestForm(forms.ModelForm):
    class Meta:
        model = Song
        exclude = ['track_id']

class PlaylistCreateForm(forms.ModelForm):
    class Meta:
        model = Playlist
        exclude = ['playlist_id', 'date_created', 'playlist_link', 'followers']
