from django import forms
from .models import Playlist

"""
name
"""

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ('playlist_name', 'playlist_link')
