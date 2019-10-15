from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


class NewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_home_page_loads(self):
        # John goes to examinator home page
        self.browser.get(self.live_server_url)

        # He can see Examinator in the title and header
        self.assertIn('Examinator', self.browser.title)
        header = self.browser.find_element_by_tag_name('h1')
        self.assertIn('Examinator', header.text)

        # There's a prominent button inviting him to create a new exam
        self.browser.set_window_size(1024, 768)
        button = self.browser.find_element_by_css_selector('button#create_exam')
        self.assertIn('new exam', button.text.lower())
        self.assertTrue(button.size['width'] > 200)
        self.assertAlmostEqual(
            button.location['x'] + button.size['width'] / 2,
            512,
            delta=10
        )
