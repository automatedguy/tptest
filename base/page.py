import logging

from selenium.webdriver.common.by import By

from json_read import JsonReader
from messages import *
from selenium.common.exceptions import NoSuchElementException
from math import radians, sin, cos, acos, sqrt


class Element:

    def __init__(self, element):
        self.element = element

    def size(self):
        return self.element.size

    def position(self):
        return self.element.location_once_scrolled_into_view

    def text(self):
        if self.element.get_attribute("value") is not None:
            element_text = str(self.element.get_attribute("value"))
        else:
            element_text = str(self.element.text)
        return element_text


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.element_ids_list = []
        self.web_elements_list = []
        self.element_a = None
        self.element_x = None
        self.closest_element = None
        self.init_min_distance = True
        self.min_distance = 0
        self.last_distance = 0

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

    def find_element_a(self, element_id):
        self.element_a = Element(self.driver.find_element(By.XPATH, element_id))
        self.logger.info(ELEMENT_A_TEXT + ': [' + self.element_a.text() + ']')
        self.logger.info(ELEMENT_A + SIZE + ': [' + str(self.element_a.size()) + ']')
        self.logger.info(ELEMENT_A + POSITION + ': [' + str(self.element_a.position()) + ']')

    def closest_element_text(self, element):
        if element.get_attribute("value") is not None:
            element_text = str(element.get_attribute("value"))
        else:
            element_text = str(element.text)
        self.logger.info(FINAL_CLOSEST_ELEMENT + ': [' + element_text + ']')

    def calculate_distance(self, element_x):
        self.logger.info('Calculating distance between upper left corners:')
        self.logger.info(ELEMENT_A + ': [' + self.element_a.text() + ']')
        self.logger.info(ELEMENT_X + ': [' + str(element_x.text()) + ']')
        self.logger.info(ELEMENT_X + POSITION + ': [' + str(element_x.position()) + ']')

        x1 = self.element_a.position()['x']
        y1 = self.element_a.position()['y']

        x2 = element_x.position()['x']
        y2 = element_x.position()['y']

        dist = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        self.logger.info('Distance between elements is : [' + str(dist) + ']')
        return dist

    def find_elements_x(self, element_id_x):
        elements_x_list = self.driver.find_elements(By.XPATH, element_id_x)
        for element in elements_x_list:
            self.last_distance = self.calculate_distance(Element(element))
            if self.init_min_distance:
                self.min_distance = self.last_distance
                self.closest_element = element
                self.init_min_distance = False
            if self.last_distance < self.min_distance:
                self.min_distance = self.last_distance
                self.closest_element = element

    def find_element_near_to(self, element_id_a, element_id_x):
        self.find_element_a(element_id_a)
        self.find_elements_x(element_id_x)
        return self.closest_element
