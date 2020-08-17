from django.test import TestCase
from django.urls import resolve

from .views import home_page


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        self.assertEqual(resolve("/").func, home_page)
