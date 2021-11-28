from django.shortcuts import render, redirect, get_object_or_404
from musicdb.models import Playlist, Song, UserEntity

from django.forms import ModelForm
from .forms import RequestForm, PlaylistForm

from django.http import Http404, JsonResponse, HttpResponseForbidden

import string, random

#####################################################################

# generates a randomized string for the playlist_id (primary key) to be indexed
def generate_playlist_id():
    letters = string.ascii_letters
    letters += string.digits

    return ''.join(random.choice(letters) for i in range(20))
