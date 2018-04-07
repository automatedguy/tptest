import logging
import os
import json
from pprint import pprint

from messages import *

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class JsonReader(object):

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def load_json(self, file_name):
        self.logger.info(OPENING_JSON_FILE + ': [' + file_name + ']')
        full_path = '../resources/' + file_name

        with open(PATH(full_path), 'r') as json_file:
            elements = json.loads(json_file.read())
            self.logger.info('Current JSON file content: ' + str(elements))
            return elements

    def get_elements(self, element_id):
        pass
