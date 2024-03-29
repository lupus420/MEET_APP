from django.http import HttpResponseRedirect
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class UsersAppViewTest(TestCase):
    def test_index_view(self):
        index_page = HttpResponseRedirect(reverse("UsersApp:index"))
        self.assertEqual(index_page.url, "/users/")

    def test_index_view_status_code(self):
        response = self.client.get(reverse("UsersApp:index"))
        self.assertEqual(response.status_code, 200)


    def test_login_view_template(self):
        response = self.client.get(reverse("UsersApp:login"))
        self.assertTemplateUsed(response, "UsersApp/login.html")
    
    def test_login_view_redirect(self):
        get_user_model().objects.create_user(username="testuser", email="test@email.com", password="testpassword")
        response = self.client.post(reverse("UsersApp:login"), {"username": "testuser", "password": "testpassword"})
        self.assertEqual(response.status_code, 302)
        
    def test_register_view_template(self):
        response = self.client.get(reverse("UsersApp:register"))
        self.assertTemplateUsed(response, "UsersApp/register.html")
    
    def test_register_view_redirect_status_code(self):
        response = self.client.post(reverse("UsersApp:register"), {"username": "testuser","email": "test@email.com", "password": "testpassword", "password_confirm": "testpassword"})
        self.assertEqual(response.status_code, 302)

    def test_register_view_redirect_template(self):
        response = self.client.post(reverse("UsersApp:register"), {"username": "testuser","email": "test@email.com", "password": "testpassword", "password_confirm": "testpassword"}, follow=True)
        self.assertTemplateUsed(response, "UsersApp/index.html")