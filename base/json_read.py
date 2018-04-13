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
        self.ids_list = []
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

    # TODO: Keep this with list comprehensions
    def iterate_elements_v2(self, element_name):
        self.logger.info(ITERATING_ELEMENTS)
        ids_list = [self.add_element(element) for element in self.json_file.items() if element[0] == element_name]
        self.append_final_list(ids_list)

    def add_element(self, element):
        self.logger.info(ELEMENT_NAME_FOUND_IN_JSON + ' :[' + str(element[0]) + ']')
        self.logger.info(ADDING_ELEMENT_ID)
        return element[1]['elementID']

    # TODO: Keep this with list comprehensions
    def iterate_finders_v2(self, element_name):
        self.logger.info(ITERATING_FINDERS)
        finders_list = self.json_file['__FINDERS__']
        ids_list = [self.get_element_id(element).replace('_ELEMENT_NAME_', element_name) for element in finders_list]
        self.append_final_list(ids_list)

    def get_element_id(self, element):
        element_id = str(element['elementID'])
        self.log_finder(element_id)
        return element_id

    def log_finder(self, element_finder):
        self.logger.info(ADDING_ELEMENT_ID_FINDER + ' :[' + element_finder + ']')
        return element_finder

    def append_final_list(self, f_ids_list):
        for f_id in f_ids_list:
            self.ids_list.append(f_id)

    def populate_element_list(self, import_file, element_name):
        self.json_file = self.load_json(import_file)
        try:
            if self.json_file['__FINDERS__'] is not None:
                self.iterate_finders_v2(element_name)
        except KeyError:
            self.iterate_elements_v2(element_name)
        return self.get_import_files_list()

    def get_element_ids_list(self, element_name):
        self.json_file = self.load_json(self._FIRST_FILE_)
        self.iterate_elements_v2(element_name)
        self.iterate_imported_list(element_name)
        self.logger.info(IDS_LIST + ' [' + str(self.ids_list) + ']')
        return self.ids_list

