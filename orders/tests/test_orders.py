from rest_framework.test import APITestCase
from products.models import Category, Product

from rest_framework.test import APIClient

from django.contrib.auth.models import User


class TestOrders(APITestCase):
    url = "/api/checkout/"

    def setUp(self):
        self.user = User.objects.create(
            username='username1',
            password='Testpass123'
        )

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        Category.objects.create(name="balls")

        self.product = Product.objects.create(
            name="pokeball",
            description="blablabla",
            price=123,
            category=Category.objects.get(name='balls')
        )

    def test_checkout(self):
        data = {
            "first_name": "Ash",
            "last_name": "Ketchum",
            "email": "ash@ketchum.kanto",
            "address": "Unknown 15",
            "zipcode": "69666",
            "city": "Alabastia",
            "phone": "69999666",
            "items": [
                {
                    "product": 1,
                    "quantity": 15,
                    "price": 15.00
                }
            ]
        }
        response = self.client.post(self.url, data=data)
        result = response.json()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(result['first_name'], 'Ash')
