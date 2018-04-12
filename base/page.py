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

    def find_element(self, element_name):
        self.logger.info(LOOKING_FOR + ': [' + element_name + ']')
        self.element_ids_list = JsonReader().get_element_ids_list(element_name)

        for element_id in self.element_ids_list:
            self.get_elements(element_id)

        self.logger.info(NUM_ELEMENTS + ' :[' + str(len(self.web_elements_list)) + ']')

        for web_element in self.web_elements_list:
            self.logger.info(LOOKING_FOR_ACTUAL_ELEMENT)
            if web_element.is_displayed():
                return web_element

    def find_element_by_id(self, element_id):
        return self.driver.find_element(By.XPATH, element_id)

    def find_element_near_to(self, element_id_a, element_id_x):
        self.element = self.find_element_by_id(element_id_a)
        element_a_size = self.size()
        element_a_position = self.position()
        self.logger.info(ELEMENT_A_TEXT + ': [' + self.element.text + ']')
        self.logger.info(ELEMENT_A + SIZE + ': [' + str(element_a_size) + ']')
        self.logger.info(ELEMENT_A + POSITION + ': [' + str(element_a_position) + ']')

        distance_a = element_a_position['x'] * element_a_position['y']
        init_min_distance = True
        min_distance = 0
        closest_element = None

        elements_x_list = self.driver.find_elements(By.XPATH, element_id_x)

        for element in elements_x_list:
            self.element = element
            position = self.position()
            distance_x = position['x'] * position['y']
            if init_min_distance:
                min_distance = abs(distance_a - distance_x) + 1
                init_min_distance = False
            if abs(distance_a - distance_x) < min_distance:
                self.logger.info(CLOSEST_ELEMENT + ': [' + str(element.get_attribute("value")) + ']')
                self.logger.info(CLOSEST_ELEMENT + ': [' + str(element.text) + ']')
                min_distance = abs(distance_a - distance_x)
                closest_element = element
        return closest_element
