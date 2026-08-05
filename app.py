password = "admin123"  # Consider removing this or using environment variables for sensitive data


def add(a, b):
    return a + b


# Make sure to break long lines to maintain less than 79 characters
very_long_variable_name_that_exceeds_the_maximum_length = (
    "This is a long string that should be broken into multiple lines."
    " Make sure to keep individual lines less than 79 characters."
)


if __name__ == "__main__":
    print(add(2, 3))
