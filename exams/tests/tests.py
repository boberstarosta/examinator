from django.test import TestCase
from exams.views import home_page_view


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


class NewExamTest(TestCase):

    def test_uses_new_exam_template(self):
        response = self.client.get('/new_exam')
        self.assertTemplateUsed(response, 'new.html')
