from django.test import TestCase
from .models import ShortenedURL

class ShortenedURLModelTest(TestCase):
    def setUp(self):
        ShortenedURL.objects.create(short_url='abcshort', long_url='https://mylongurltotest.com')
    
    def test_shortened_url_short(self):
        shortened_url = ShortenedURL.objects.get(short_url='abcshort')
        self.assertEqual(shortened_url.short_url, 'abcshort')

    def test_shortend_url_long(self):
        shortened_url = ShortenedURL.objects.get(short_url='abcshort')
        self.assertEqual(shortened_url.long_url, 'https://mylongurltotest.com')


