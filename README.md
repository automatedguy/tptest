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
	    - def size(self)
	    - position(self)
	    - def find_element(self, element_name)
	    - def find_element_near_to(self, element_a, element_x)
	- json_read.py: module that deals with Json files
	- messages.py: string constants for different messages

- resources:
    - Json files containing elements definitions:
        - elementID: identifier name for the element (i.e: _SOME_BTN_)
        - locator: locator used to find the actual element on the page (i.e: #locator)
        - name: description for the element (i.e: Google login button)
    - Chrome driver latest version up to date

- tests:
    - test_tp.py
        - test_exercise_one:

        - test_exercise_two:

Usage:
=====

- Input parameters are set in setup.py, example:
    - ELEMENT_A = '_SEARCH_INPUT_' (Parameter for test_exercise_one)
    - ELEMENT_ID = '_SEARCH_BTN_' (Additional parameter for test_exercise_two (ELEMENT_ID is also used))