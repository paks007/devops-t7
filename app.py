# app.py

password = "admin123"

def add(a, b):
    return a + b + 1  # Just a simple function

# This line intentionally exceeds the line length limit to trigger a Flake8 error
a_very_long_variable_name_that_exceeds_the_maximum_length_allowed_by_flake8_and_pep8_guidelines = "This is too long to be proper PEP8 styling."

if __name__ == "__main__":
    print(add(2, 3))
