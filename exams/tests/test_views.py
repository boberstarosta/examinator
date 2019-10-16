from django.test import TestCase
from django.urls import reverse
from exams.views import home_page_view
from exams.models import Exam
from exams.forms import NewExamForm


class HomePageViewTest(TestCase):

    def test_root_url_resolves_to_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_contains_create_new_exam_button(self):
        response = self.client.get('/')
        create_exam_url = reverse('create_exam')
        self.assertContains(response, f'href="{create_exam_url}"')


class CreateExamViewTest(TestCase):

    def test_uses_create_exam_template(self):
        response = self.client.get('/exams/new/')
        self.assertTemplateUsed(response, 'create_exam.html')

    def test_uses_new_exam_form(self):
        response = self.client.get('/exams/new/')
        self.assertIsInstance(response.context['form'], NewExamForm)
