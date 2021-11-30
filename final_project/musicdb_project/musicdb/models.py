from django.db import models
from django.apps import apps

#user_entity = apps.get_model('users', 'UserEntity')

class Song(models.Model):
    song_id = models.TextField(primary_key = True)
    song_artists = models.TextField()
    song_name = models.TextField()
    song_link = models.TextField()

    def __str__(self):
        return self.song_name

class Playlist(models.Model):
    playlist_id = models.TextField(primary_key=True)
    playlist_name = models.TextField()
    followers = models.IntegerField()
    owner_name = models.ForeignKey('users.UserEntity', on_delete=models.CASCADE)
    date_created = models.DateField()
    playlist_link = models.TextField()
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.playlist_name
