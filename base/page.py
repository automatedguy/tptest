import logging

from selenium.webdriver.common.by import By

from json_read import JsonReader
from messages import *
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    def __init__(self, driver):
        self.logger = logging.getLogger(__name__)
        self.element_list = None
        self.element = None
        self.driver = driver

    def find_element(self, element_name):
        self.element_list = JsonReader().get_elements(element_name)
        for element in self.element_list:
            try:
                self.logger.info(WAITING_FOR + element_name)
                locator = (By.CSS_SELECTOR, element['locator'])
                self.element = WebDriverWait(self.driver, 7).until(
                    EC.presence_of_element_located(locator)
                )
                self.logger.info(ELEMENT_FOUND)
            except TimeoutException:
                self.logger.info(ELEMENT_NOT_FOUND)
        return self.element

    def size(self):
        pass

    def position(self):
        pass

    def find_element_near_to(self):
        pass