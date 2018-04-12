Total Performance Exam
======================

Suggested system requirements:
=============================
- Chrome Browser Version 65
- Python 3

Project Structure:
=================

- base:

	- setup.py: base test setup class

	- page.py: base page class

	    - def get_elements(self, element_id):
	        receives an elementID and returns a list of all element objects found with this elementID.

	    - def size(self):
	        returns the width and height of the element.

	    - def position(self):
	        returns a position x and y of the element's top-left corner.

	    - def find_element(self, element_name):
	        receives an element name to find the element, return an element object or a None value if not found.

	    - def find_element_near_to(self, element_a, element_x):
	        receives an element A and an elementID X and returns the element object of the element with elementID X that is nearest to element A

	- json_read.py: module that deals with Json files

	    - def load_json(self, file_name): receives the file name and returns the contained dictionary.

	- messages.py: string constants for different messages

- resources: element files and driver

    - Json files containing elements definitions and __FINDERS__ (examples):

          "ElementName": {
            "elementID": "//input[@value = \"Buscar con Google\"]",
            "description": "Google search button"
          }

          "__FINDERS__": [
            {
                "elementID": "//*[@id=\"fsr\"]/a[text() = \"_ELEMENT_NAME_\"]",
                "description": "Element found by text"
            }
          ]

    - Json file list and content:

        - center.json: Google search page center web elements definitions

        - header.json: Google search page header section __FINDERS__

        - footer_left.json: Google search page left side footer web elements definitions

        - footer_right.json: Google search page right side __FINDERS__

    - Chrome driver latest version up to date

- tests:

    - test_tp.py:

        - test_exercise_one:

        - test_exercise_two:

Usage:
=====

- Input parameters are set in setup.py, examples:

    - Parameter for test_exercise_one (ElementName):
        - ELEMENT_NAME = 'Buscar con Google'

    - Parameters for test_exercise_two (elementID):
        - ELEMENT_ID_A = '//input[@value = \"Buscar con Google\"]'
        - ELEMENT_ID_X = '//input[@value = \"Me siento con suerte \"]'