from django.test import TestCase, Client
from django.urls import resolve
from cart import views

class Test(TestCase):
    def test_response_code(self):
        urls = [
            "/cart/", "/cart/add/?id=1", "/cart/remove/?id=1", 
            "/cart/chosen-ids/", "/cart/remove-all/"
        ]
        
        for url in urls:
            response = self.client.get(url)
            self.assertEquals(response.status_code, 200)

    def test_views_mapping(self):
        dict = { 
            "/cart/": views.index,
            "/cart/chosen-ids/": views.chosenIds,
            "/cart/remove-all/": views.removeAll,
            "/cart/add/": views.add,
            "/cart/remove/": views.remove
        }

        for key, val in dict.items():
            view = resolve(key)
            self.assertEquals(view.func, val)  


    def test_scenario(self):
        client = Client()
        response = client.get("/cart/add/?id=1")
        self.assertEquals(response.status_code, 200)
        
        response = client.get("/cart/chosen-ids/")
        self.assertEquals(response.json(), [1])

        response = client.get("/cart/add/?id=2")
        self.assertEquals(response.status_code, 200)
        
        response = client.get("/cart/chosen-ids/")
        self.assertEquals(response.json(), [1, 2])

        response = client.get("/cart/remove/?id=1")
        self.assertEquals(response.status_code, 200)

        response = client.get("/cart/chosen-ids/")
        self.assertEquals(response.json(), [2])

        response = client.get("/cart/remove-all/")
        self.assertEquals(response.status_code, 200)

        response = client.get("/cart/chosen-ids/")
        self.assertEquals(response.json(), [])


# Create your tests here.
