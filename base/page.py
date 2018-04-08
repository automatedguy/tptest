import logging
from json_read import JsonReader
from messages import *
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.element_list = None

    def get_element_list(self, element_name):
        self.element_list = JsonReader().get_elements(element_name)

    def find_element(self, element_name):
        self.get_element_list(element_name)
        for element in self.element_list:
            try:
                self.logger.info(WAITING_FOR + element_name)
                element = WebDriverWait(self.driver, 7).until(
                    EC.presence_of_element_located(element['locator'])
                )
                return element
            except TimeoutException:
                return None

    def size(self):
        pass

    def position(self):
        pass

    def find_element_near_to(self):
        pass