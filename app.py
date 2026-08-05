password = "admin123"  # This could also be a concern, but keep it for demonstration purposes

# Intentionally creating a long line to fail flake8
def add(a, b):
    return a + b  # This line is too simple, let's create a violation next
print("This is a very long line to intentionally trigger a line length violation in Flake8. " +
      "It exceeds the maximum allowed length of 79 characters and thus should cause " +
      "the pipeline to fail due to code quality checks.")

if __name__ == "__main__":
    print(add(2, 3))
