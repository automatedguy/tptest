import logging

from selenium.webdriver.common.by import By

from json_read import JsonReader
from messages import *
from selenium.common.exceptions import NoSuchElementException
from math import radians, sin, cos, acos


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
        slat = radians(float(self.element_a.position()['x']))
        slon = radians(float(self.element_a.position()['y']))
        elat = radians(float(element_x.position()['x']))
        elon = radians(float(element_x.position()['x']))

        dist = 6371.01 * acos(sin(slat) * sin(elat) + cos(slat) * cos(elat) * cos(slon - elon))
        return dist

    def find_elements_x(self, element_id_x):
        elements_x_list = self.driver.find_elements(By.XPATH, element_id_x)
        init_min_distance = True
        for element in elements_x_list:
            last_distance = self.calculate_distance(Element(element))
            if init_min_distance:
                min_distance = last_distance
                self.closest_element = element
                init_min_distance = False
            if last_distance > min_distance:
                min_distance = last_distance
                self.closest_element = element

    def find_element_near_to(self, element_id_a, element_id_x):
        self.find_element_a(element_id_a)
        self.find_elements_x(element_id_x)
        return self.closest_element
