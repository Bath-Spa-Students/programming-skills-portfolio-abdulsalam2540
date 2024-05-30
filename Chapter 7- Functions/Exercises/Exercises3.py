def make_shirt(size, message):
    """Prints a sentence summarizing the size of the shirt and the message printed on it."""
    print(f"A {size}-sized shirt will be made with the message: '{message}'.")

# Call the function using positional arguments
make_shirt("medium", "Hello, World!")

# Call the function using keyword arguments
make_shirt(size="large", message="Python Rocks!")
