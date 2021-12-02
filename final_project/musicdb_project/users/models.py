from django.db import models
from django.apps import apps
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import date
from PIL import Image

#song_model = apps.get_model('musicdb', 'Song')
#playlist_model = apps.get_model('musicdb', 'Playlist')

# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, country, password=None):
        if not username:
            raise ValueError('Users must have a username')
        if not first_name:
            raise ValueError('Users must have a first name')
        if not last_name:
            raise ValueError('Users must have a last name')
        if not country:
            raise ValueError('Users must have a country')

        user = self.model(
            username = username,
            first_name = first_name,
            last_name = last_name,
            country = country,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, user, first_name, last_name, country, password):
        user = self.create_user(
            username = user,
            first_name = first_name,
            last_name = last_name,
            country = country,
            password = password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.set_password(password)
        user.save(using=self._db)

        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.TextField(default=None)
    image = models.ImageField(default='avatars/default.png', upload_to='avatars')

    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    playlist_count = models.IntegerField(default=0)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = AccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return self.is_admin

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def user_playlists(self):
        return self.playlists.all()

    def is_following(self):
        return self.following.all()

    def followed_by(self):
        return self.followers.all()

    class Meta:
        ordering = ('-date_joined',)

class UserFollowing(models.Model):
    username = models.ForeignKey("User", related_name="following", on_delete=models.CASCADE)
    following_username = models.ForeignKey("User", related_name="followers", on_delete=models.CASCADE, default=None)
    started_following = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['username', 'following_username']
