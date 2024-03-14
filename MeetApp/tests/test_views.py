import os
from django import setup
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MEET_APP.settings")
setup()

from django.http import HttpResponseRedirect
from django.test import TestCase
from django.urls import reverse
from MeetApp.views import index
from django.contrib.auth import get_user_model

User = get_user_model()

class MeetAppViewTest(TestCase):
    def test_index_view(self):
        index_page = HttpResponseRedirect(reverse("MeetApp:index"))
        self.assertEqual(index_page.url, "/")

    def test_index_view_status_code(self):
        response = self.client.get(reverse("MeetApp:index"))
        self.assertEqual(response.status_code, 200)

    def test_index_view_template(self):
        response = self.client.get(reverse("MeetApp:index"))
        self.assertTemplateUsed(response, "MeetApp/index.html")