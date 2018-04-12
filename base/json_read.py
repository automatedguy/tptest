import logging
import os
import json
from messages import *

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class JsonReader(object):

    _FIRST_FILE_ = 'center'
    _JSON_ = '.json'
    _RESOURCES_ = '../resources/'

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.json_file = None
        self.raw_data = None
        self.element_ids_list = []
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

    def iterate_imported_list(self, element_name):
        import_files_list = self.get_import_files_list()
        while import_files_list:
            additional_files = self.populate_element_list(import_files_list[0], element_name)
            import_files_list.pop(0)
            for file in additional_files:
                import_files_list.append(file)

    def iterate_elements(self, element_name):
        self.logger.info(ITERATING_ELEMENTS)
        for element in self.json_file.items():
            if element[0] == element_name:
                self.logger.info(ELEMENT_NAME_FOUND_IN_JSON + ' :[' + str(element[0]) + ']')
                self.logger.info(ADDING_ELEMENT_ID)
                self.element_ids_list.append(element[1]['elementID'])

    def iterate_finders(self, element_name):
        self.logger.info(ITERATING_FINDERS)
        for element in self.json_file['__FINDERS__']:
            element_finder = str(element['elementID']).replace('_ELEMENT_NAME_', element_name)
            self.logger.info(ADDING_ELEMENT_ID_FINDER + ' :[' + element_finder + ']')
            self.element_ids_list.append(element_finder)

    def populate_element_list(self, import_file, element_name):
        self.json_file = self.load_json(import_file)
        try:
            if self.json_file['__FINDERS__'] is not None:
                self.iterate_finders(element_name)
        except KeyError:
            self.iterate_elements(element_name)
        return self.get_import_files_list()

    def get_element_ids_list(self, element_name):
        self.json_file = self.load_json(self._FIRST_FILE_)
        self.iterate_elements(element_name)
        self.iterate_imported_list(element_name)
        self.logger.info(IDS_LIST + ' [' + str(self.element_ids_list) + ']')
        return self.element_ids_list

