from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient


class APILoginViewTestCase(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.data = {
            "username": "admin",
            "password": "admin1234"
        }

    def test_create_user(self):

        user = User.objects.create_user(**self.data)
        user.save()

    def test_login(self):
        self.test_create_user()
        response = self.client.post('/login/api-token-auth/', self.data, format="json")
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.json().get("token"))
