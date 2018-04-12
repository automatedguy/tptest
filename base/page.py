import logging

from selenium.webdriver.common.by import By

from json_read import JsonReader
from messages import *
from selenium.common.exceptions import NoSuchElementException


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.element_ids_list = []
        self.web_elements_list = []
        self.element = None

    def size(self):
        return self.element.size

    def position(self):
        return self.element.location_once_scrolled_into_view

    def get_elements(self, element_id):
        try:
            web_element = self.driver.find_element(By.XPATH, element_id)
            self.logger.info(ELEMENT_IS_THERE)
            self.web_elements_list.append(web_element)
        except NoSuchElementException:
            self.logger.info(ELEMENT_NOT_FOUND)
        pass

    def find_element(self, element_name):
        self.logger.info(LOOKING_FOR + ': [' + element_name + ']')

        self.element_ids_list = JsonReader().get_element_ids_list(element_name)

        for element_id in self.element_ids_list:
            self.get_elements(element_id)

        for web_element in self.web_elements_list:
            if web_element.is_displayed():
                return web_element

    def find_element_near_to(self, element_a, element_x):
        self.element = self.find_element(element_a)
        element_a_size = self.size()
        element_a_position = self.position()
        self.logger.info(ELEMENT_A + SIZE + ': [' + str(element_a_size) + ']')
        self.logger.info(ELEMENT_A + POSITION + ': [' + str(element_a_position) + ']')

        self.logger.info(LOOKING_FOR + ': [' + element_x + ']')
        self.element_ids_list = JsonReader().get_elements(element_x)

        distance_a = element_a_position['x'] * element_a_position['y']
        init_min_distance = True
        min_distance = 0
        closest_element = None

        for element in self.element_ids_list:
            try:
                self.element = self.driver.find_element(By.CSS_SELECTOR, element['locator'])
                position = self.position()
                distance_x = position['x'] * position['y']
                if init_min_distance:
                    min_distance = abs(distance_a - distance_x) + 1
                    init_min_distance = False
                if abs(distance_a - distance_x) < min_distance:
                    self.logger.info('Closest element now is :[' + element['name'] + ']')
                    min_distance = abs(distance_a - distance_x)
                    closest_element = self.element
            except NoSuchElementException:
                self.logger.info('Element was not there.')
        return closest_element
