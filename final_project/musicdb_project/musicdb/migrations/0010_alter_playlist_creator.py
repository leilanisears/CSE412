# Generated by Django 3.2.9 on 2021-12-01 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20211201_2338'),
        ('musicdb', '0009_rename_owner_name_playlist_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]