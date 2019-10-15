from django.test import LiveServerTestCase
from selenium import webdriver


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_home_page_loads(self):
        # John goes to examinator home page
        self.browser.get(self.live_server_url)
        # He can see Examinator in the title
        self.assertIn('Examinator', self.browser.title)
