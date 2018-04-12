import os
import test
import unittest
import logging
from selenium import webdriver

from base.messages import *

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

# Just the base URL.
BASE_URL = 'https://www.google.com'

# Tests input parameters:
# Parameter for: test_exercise_one
ELEMENT_NAME = 'Gmail'
# Additional parameter for: test_exercise_two (ELEMENT_ID is also used)
ELEMENT_ID_A = '_SEARCH_INPUT_'
ELEMENT_ID_X = '_SEARCH_INPUT_'


class BaseTest(unittest.TestCase):

    base_url = BASE_URL
    element_name = ELEMENT_NAME

    element_id_a = ELEMENT_ID_A
    element_id_x = ELEMENT_ID_X
    path = PATH

    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)
    chrome_path = '../resources/chromedriver'

    @classmethod
    def setUpClass(cls):
        """Run our `setUp` method on inherited classes, """
        if cls is not BaseTest and cls.setUp is not BaseTest.setUp:
            orig_setUp = cls.setUp

            def setUpOverride(self, *args, **kwargs):
                BaseTest.setUp(self)
                return orig_setUp(self, *args, **kwargs)

            cls.setUp = setUpOverride

    def start_browser(self):
        self.logger.info(STARTING_BROWSER)
        self.driver = webdriver.Chrome(PATH(self.chrome_path))
        self.logger.info(BROWSER_STARTED)

    def maximize_browser(self):
        self.logger.info(MAXIMIZING_WINDOW)
        self.driver.maximize_window()
        self.logger.info(WINDOW_MAXIMIZED)

    def open_base_url(self):
        self.logger.info(OPENING_BASE_URL + '[' + self.base_url + ']')
        self.driver.get(self.base_url)

    def close_browser(self):
        self.logger.info(CLOSING_BROWSER)
        self.driver.quit()
        self.logger.info(BROWSER_CLOSED)

    def setUp(self):
        self.start_browser()
        self.maximize_browser()
        self.open_base_url()
        pass

    def tearDown(self):
        self.close_browser()
        pass


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromModule(test)
    results = unittest.TextTestRunner(verbosity=2).run(suite)
