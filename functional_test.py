import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./../chromedriver.exe')

    def tearDown(self):
        self.driver.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.driver.get('http://localhost:8000')

        self.assertIn('To-Do', self.driver.title)

        self.fail('finish the test')


if __name__ == "__main__":
    unittest.main()
