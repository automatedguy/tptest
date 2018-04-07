import logging


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def find_element(self):
        pass

    def size(self):
        pass

    def position(self):
        pass

    def find_element_near_to(self):
        pass