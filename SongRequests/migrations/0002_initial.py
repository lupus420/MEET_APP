# Generated by Django 5.0.3 on 2024-03-13 22:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("SongRequests", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="playlist",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="playlists",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="playlistsong",
            name="playlist",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="SongRequests.playlist"
            ),
        ),
        migrations.AddField(
            model_name="song",
            name="added_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="songs",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="playlistsong",
            name="song",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="SongRequests.song"
            ),
        ),
        migrations.AddField(
            model_name="playlist",
            name="songs",
            field=models.ManyToManyField(
                blank=True,
                related_name="parent_playlists",
                through="SongRequests.PlaylistSong",
                to="SongRequests.song",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="playlistsong",
            unique_together={("playlist", "song")},
        ),
    ]
