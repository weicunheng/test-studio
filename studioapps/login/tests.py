from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient


class APILoginViewTestCase(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.data = {
            "username": "test",
            "password": "test1234."
        }

    def test_create_user(self):

        user = User.objects.create_user(**self.data)
        user.save()

    def test_login(self):
        self.test_create_user()
        response = self.client.post('/login/', self.data, format="json")
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.json().get("token"))
