from rest_framework.test import APITestCase


class TestUsers(APITestCase):
    url = "/api/users/"

    def test_create_user(self):
        """Test creating a new user"""
        data = {
            "username": "username1",
            "password": "Testpass123"
        }

        response = self.client.post(self.url, data=data)
        result = response.json()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(result['username'], "username1")
