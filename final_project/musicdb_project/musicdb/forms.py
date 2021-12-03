from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from .models import Playlist, Song

"""
name
"""


class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ('playlist_name', 'playlist_link',)

class BuilderForm(forms.ModelForm):
    class Meta:
        model = Playlist
        songs = forms.ModelMultipleChoiceField(Song.objects.all())
        fields = ('playlist_id', 'playlist_name', 'playlist_link', 'songs',)

