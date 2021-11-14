from django.db import models
from django.apps import apps

#user_entity = apps.get_model('users', 'UserEntity')
class Playlist(models.Model):
    playlist_id = models.TextField(primary_key=True)
    followers = models.IntegerField()
    owner_name = models.ForeignKey('users.UserEntity', on_delete=models.CASCADE)
    date_created = models.DateField()
    playlist_link = models.TextField()

class Song(models.Model):
    song_id = models.TextField(primary_key = True)
    artist_name = models.TextField()
    song_name = models.TextField()
    song_link = models.TextField()
    duration = models.DurationField()
