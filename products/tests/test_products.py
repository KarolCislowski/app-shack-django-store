from rest_framework.test import APITestCase
from products.models import Category, Product

from rest_framework.test import APIClient

from django.contrib.auth.models import User


class TestProduct(APITestCase):
    url = "/api/products/"
    url_admins = "/api/admin/products"

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

        Category.objects.create(name="balls")

        Product.objects.create(
            name="pokeball",
            description="blablabla",
            price=123,
            category=Category.objects.get(name='balls')
        )

    def test_get_product(self):

        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(result[0]['name'], 'pokeball')

    def test_delate_product(self):
        id = "1"

        self.client.force_authenticate(user=self.admin)
        response = self.client.delete(
            self.url_admins + f"/{id}")

        self.assertEqual(response.status_code, 204)
