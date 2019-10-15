from django.test import TestCase
from exams.views import home_page_view


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
