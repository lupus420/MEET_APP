# Generated by Django 5.0.3 on 2024-03-13 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Playlist",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=64, unique=True)),
                ("anonymous", models.BooleanField(default=False)),
                ("add_date", models.DateTimeField(auto_now_add=True, null=True)),
                ("last_modified", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="PlaylistSong",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("add_date", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["add_date"],
            },
        ),
        migrations.CreateModel(
            name="Song",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=64)),
                ("artist", models.CharField(blank=True, max_length=64, null=True)),
                ("url_field", models.URLField(blank=True, null=True)),
                ("add_date", models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
