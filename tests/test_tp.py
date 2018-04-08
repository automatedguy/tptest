from base.setup import BaseTest
from base.messages import *
from page import BasePage


class Exercises(BaseTest):

    def setUp(self):
        self.logger.info(STARTING)
        self.base_page = BasePage(self.driver)

    def test_exercise_one(self):
        self.logger.info(EXERCISE_ONE)
        self.logger.info('Looking for element : ' + self.element_id)
        self.base_page.find_element(self.element_id)

    def test_exercise_two(self):
        self.logger.info(EXERCISE_TWO)
        self.logger.info('Element A is: [' + self.element_a + ']')
        self.logger.info('ElementID is: [' + self.element_id)
