import logging
import os
import json

from messages import *

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class JsonReader(object):

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.elements = None
        self.raw_data = None

    def load_json(self, file_name):
        self.logger.info(OPENING_JSON_FILE + ': [' + file_name + ']')
        full_path = '../resources/' + file_name

        with open(PATH(full_path), 'r') as json_file:
            self.raw_data = json_file.read()
            elements = json.loads(self.raw_data)
            self.logger.info('Current JSON file content: ' + str(elements))
            return elements

    def get_elements(self, element_id):
        
        self.elements = self.load_json('file1.json')
        for element in self.elements.items():
            try:
                if element[1]['elementID'] is element_id:
                    return element[1]
            except TypeError:
                self.logger.info('Type error catch.')
        return None
