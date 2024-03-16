Project Description:
This project is designed to assess web development assignments submitted by users. It includes a folder structure to mimic the typical submission format, with separate directories for assignments and validators.

Folder Structure:
assignment: Contains the user-submitted web development assignments.
validators: Includes Python files responsible for testing the code present in the assignment folder.

    html_validator.py: Validates HTML code.
    css_validator.py: Validates CSS code.
    javascript_validator.py: Validates JavaScript code.

criteria.yml: This file outlines all the criteria against which the web assignment will be evaluated.

Functionality:
The project evaluates whether HTML tags, CSS classes, and JavaScript functions meet the specified criteria outlined in the criteria.yml file. The validation process is initiated by running validator.py.

How to Run:
Install all the requirements listed in requirements.txt.
Execute validator.py to initiate the validation process.