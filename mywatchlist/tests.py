from urllib import response
from django.test import TestCase, Client

# Create your tests here.
class MyWatchListTest(TestCase):
    def test_mywatchlist_app_url_exists(self):
        response = Client().get('/mywatchlist')
        self.assertEqual(response.status_code,200)

    def test_mywatchlist_app_url_exists(self):
        response = Client().get('/mywatchlist/html/')
        self.assertEqual(response.status_code,200)

    def test_mywatchlist_app_url_exists(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code,200)

    def test_mywatchlist_app_url_exists(self):
        response = Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)