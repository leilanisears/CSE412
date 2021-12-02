from django.db import models
from django.apps import apps
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.utils.crypto import get_random_string
from users.models import User

#user_entity = apps.get_model('users', 'UserEntity')

class Song(models.Model):
    song_id = models.TextField(primary_key = True)
    song_artists = models.TextField()
    song_name = models.TextField()
    song_link = models.TextField()

    likes = models.ManyToManyField(User, blank=True, related_name='songLikes')

    def __str__(self):
        return self.song_name

    def save (self, *args, **kwargs):
        super().save(*args, **kwargs)


    # For if we need to slug song primary key as well
    # def get_absolute_url(self):
    #     return reverse("playlist-detail", args=[self.song_id])


class Playlist(models.Model):
    playlist_id = models.SlugField(primary_key=True, max_length=100)
    playlist_name = models.TextField(default='My Playlist')
    followers = models.IntegerField(default=0)
    creator = models.ForeignKey('users.User', on_delete=models.CASCADE)
    shares = models.ManyToManyField(User, blank=True, related_name='playlistShares')
    likes = models.ManyToManyField(User, blank=True, related_name='playlistLikes')

    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    playlist_link = models.TextField(default='https://spotify.com')
    songs = models.ManyToManyField(Song, blank=True)

    def __str__(self):
        return self.playlist_name

    def unique_slugify(self, slug):
        model = self.__class__
        unique_slug = slug
        while model.objects.filter(playlist_id=unique_slug).exists():
            unique_slug = slug + get_random_string(length = 2)
        return unique_slug

    def save (self, *args, **kwargs):
        if not self.playlist_id:
            self.playlist_id = self.unique_slugify(slugify(self.playlist_name))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("playlist-detail", args=[self.playlist_id])
