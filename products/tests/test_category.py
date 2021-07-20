from rest_framework.test import APITestCase
from products.models import Category

from rest_framework.test import APIClient

from django.contrib.auth.models import User


class TestCategory(APITestCase):
    url = "/api/categories/"
    url_admins = "/api/admin/categories"

    def setUp(self):
        self.user = User.objects.create(
            username='username1',
            password='Testpass123'
        )

        self.admin = User.objects.create_superuser(
            username='admin',
            password='Passtest123'
        )

        self.client = APIClient()

        Category.objects.create(name="potions")

    def test_get_category(self):

        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(result[0]['name'], 'potions')

    def test_post_category(self):
        data = {
            "name": "balls",
        }
        self.client.force_authenticate(user=self.admin)
        response = self.client.post(self.url_admins, data=data)
        result = response.json()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(result['name'], 'balls')

    def test_update_category(self):
        id = "1"
        data = {
            "name": "lures",
        }
        self.client.force_authenticate(user=self.admin)
        response = self.client.patch(
            self.url_admins + f"/{id}", data=data)
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['name'], 'lures')

    def test_delate_category(self):
        id = "1"

        self.client.force_authenticate(user=self.admin)
        response = self.client.delete(
            self.url_admins + f"/{id}")

        self.assertEqual(response.status_code, 204)
