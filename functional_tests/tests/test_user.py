from selenium import webdriver
from selenium.webdriver.common.by import By
from django.test import LiveServerTestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)  # Adjust based on your needs
        self.user = User.objects.create_user(username="testuser", password="testpassword", email="user@email.com")

    def tearDown(self):
        self.browser.quit()

    def login(self):
        self.browser.get(self.live_server_url + "/users/login")
        self.browser.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys("testuser")
        self.browser.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("testpassword")
        self.browser.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    def test_user_login(self):
        self.login()
        self.assertIn("You are logged in", self.browser.page_source)

    def test_user_logout(self):
        self.login()
        self.browser.find_element(By.LINK_TEXT, "Logout").click()
        self.assertIn("Logged out", self.browser.page_source)

    def test_user_register(self):
        self.browser.get(self.live_server_url + "/users/register")
        self.browser.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys("newuser")
        self.browser.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("newuser@email.com")
        self.browser.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("n3wPas5word")
        self.browser.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        self.assertIn("You are logged in", self.browser.page_source)
