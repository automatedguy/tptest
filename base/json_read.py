import logging
import os
import json

from messages import *

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class JsonReader(object):

    _FIRST_FILE_ = 'file1'
    _JSON_ = '.json'
    _RESOURCES_ = '../resources/'

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.json_file = None
        self.raw_data = None
        self.element_list = []

    def load_json(self, file_name):
        full_path = self._RESOURCES_ + file_name + self._JSON_
        self.logger.info(OPENING_JSON_FILE + ': [' + full_path + ']')

        with open(PATH(full_path), 'r') as json_file:
            self.raw_data = json_file.read()
            elements = json.loads(self.raw_data)
            self.logger.info(CURRENT_JSON_CONTENT + ' :[' + str(elements) + ']')
            return elements

    def get_import_files_list(self):
        return self.json_file['import']

    def iterate_json_one(self, element_id):
        for element in self.json_file.items():
            try:
                if element[1]['elementID'] == element_id:
                    self.element_list.append(element[1])
            except TypeError:
                self.logger.info(TYPE_ERROR)

    def iterate_json_two(self, element_id):
        for element in self.json_file['__FINDERS__'].items():
            try:
                if element['elementID'] == element_id:
                    self.element_list.append(element[1])
            except TypeError:
                self.logger.info(TYPE_ERROR)

    def populate_element_list(self, import_file, element_id):
        self.json_file = self.load_json(import_file)
        try:
            self.iterate_json_one(element_id)
        except TypeError:
            self.iterate_json_two(element_id)

    def get_elements(self, element_id):
        self.json_file = self.load_json(self._FIRST_FILE_)
        import_files_list = self.get_import_files_list()
        self.iterate_json_one(element_id)

        for import_file in import_files_list:
            self.populate_element_list(import_file, element_id)

        return self.element_list
