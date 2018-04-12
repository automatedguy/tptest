from base.setup import BaseTest
from base.messages import *
from page import BasePage


class Exercises(BaseTest):

    def __init__(self, driver):
        super(Exercises, self).__init__(driver)
        self.driver = driver

    def setUp(self):
        self.logger.info(STARTING)
        self.base_page = BasePage(self.driver)

    def test_exercise_one(self):
        self.logger.info(EXERCISE_ONE)
        element = self.base_page.find_element(self.element_name)
        self.assertIsNotNone(element)
        self.logger.info(ELEMENT_FOUND + ': [' + self.element_name + ']')

    def test_exercise_two(self):
        self.logger.info(EXERCISE_TWO)
        element = self.base_page.find_element_near_to(self.element_id_a, self.element_id_x)
        self.assertIsNotNone(element)
        self.logger.info(CLOSEST_ELEMENT_FOUND + ': [' + element.get_attribute("value") + ']')
