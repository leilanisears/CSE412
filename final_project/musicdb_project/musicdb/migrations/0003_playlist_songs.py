# Generated by Django 3.2.9 on 2021-11-18 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicdb', '0002_auto_20211114_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='songs',
            field=models.ManyToManyField(to='musicdb.Song'),
        ),
    ]