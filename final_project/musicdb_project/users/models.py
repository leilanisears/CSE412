from django.db import models
from django.apps import apps

#song_model = apps.get_model('musicdb', 'Song')
#playlist_model = apps.get_model('musicdb', 'Playlist')

# Create your models here.

class UserEntity(models.Model):
    user_id = models.TextField(primary_key=True)
    likes = models.ForeignKey('musicdb.Song', on_delete=models.CASCADE, related_name='songs')
    shares = models.ForeignKey('musicdb.Playlist', on_delete=models.CASCADE, related_name='playlists')
    playlist_count = models.IntegerField()
    country = models.TextField()
    display_name = models.TextField()
    image = models.TextField()
    playlists = models.ForeignKey('musicdb.Playlist', on_delete=models.CASCADE)
