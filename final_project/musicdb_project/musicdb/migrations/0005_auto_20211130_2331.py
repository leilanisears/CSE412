# Generated by Django 3.2.9 on 2021-11-30 23:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicdb', '0004_playlist_playlist_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='artist_name',
            new_name='song_artists',
        ),
        migrations.RemoveField(
            model_name='song',
            name='duration',
        ),
    ]
