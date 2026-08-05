# If this is the problematic long line:
password = "a_very_long_string_that_is_intentionally_made_long_to_test_flake8"

# Change it to something like this:
password = (
    "a_very_long_string_that_is_intentionally_made_long_"
    "to_test_flake8"
)

def add(a, b):
    return a + b


def another_function():
    print("Some functionality")

if __name__ == "__main__":
    print(add(2, 3))
