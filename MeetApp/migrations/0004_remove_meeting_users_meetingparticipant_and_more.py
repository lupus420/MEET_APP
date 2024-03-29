# Generated by Django 5.0.3 on 2024-03-26 20:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("MeetApp", "0003_meeting_creator"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="meeting",
            name="users",
        ),
        migrations.CreateModel(
            name="MeetingParticipant",
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
                (
                    "meeting",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="MeetApp.meeting",
                    ),
                ),
                (
                    "participant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Meeting Participant",
                "verbose_name_plural": "Meeting Participants",
                "unique_together": {("participant", "meeting")},
            },
        ),
        migrations.AddField(
            model_name="meeting",
            name="participants",
            field=models.ManyToManyField(
                blank=True,
                related_name="meetings",
                through="MeetApp.MeetingParticipant",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
