from django.test import TestCase
from django.urls import reverse

class Test(TestCase):
    def test(self):
        response = self.client.get("/shop/")
        self.assertEquals(response.status_code, 200)

# Create your tests here.
