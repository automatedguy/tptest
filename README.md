Total Performance Exam
======================

Suggested system requirements:
=============================
- Chrome Browser Version 65
- Python 3

Project Structure:
=================

- base:
	- setup: base test setup class
	- page: base page class
	- json_read: module that deals with Json files
	- messages: string constants for different messages

- resources:
    - Json files containing elements definitions:
        - elementID: identifier name for the element example: (i.e: _SOME_BTN_)
        - locator: locator used to find the actual element on the page (i.e: #locator)
        - name: description for the element (i.e: Google login button)
    - Chrome driver latest version up to date

- tests:
    - test_tp
        - test_exercise_one
        - test_exercise_two

Usage:
=====

- Input parameters are set in setup.py, example:
    - ELEMENT_A = '_SEARCH_INPUT_'
    - ELEMENT_ID = '_SEARCH_BTN_'