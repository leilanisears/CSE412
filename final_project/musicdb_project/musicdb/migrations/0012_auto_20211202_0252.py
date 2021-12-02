# Generated by Django 3.2.9 on 2021-12-02 02:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('musicdb', '0011_auto_20211202_0225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='playlistLikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='shares',
            field=models.ManyToManyField(blank=True, related_name='playlistShares', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='songs',
            field=models.ManyToManyField(blank=True, to='musicdb.Song'),
        ),
        migrations.AlterField(
            model_name='song',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='songLikes', to=settings.AUTH_USER_MODEL),
        ),
    ]