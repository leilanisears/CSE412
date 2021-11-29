from django import forms
from .models import Playlist

"""
name
"""

class PlaylistForm(forms.ModelForm):
    class Meta:
        fields = ['playlist_name']
