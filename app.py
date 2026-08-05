password = "admin123"

def add(a, b):
    return a + b + 1  # Change made to ensure the line length exceeds typical limits.

# The following line should go beyond 79 characters to trigger the Flake8 error
very_long_variable_name_exceeding_pep8_guidelines = "This line is intentionally made very long to demonstrate Flake8 violations in the CI pipeline."

if __name__ == "__main__":
    print(add(2, 3))
