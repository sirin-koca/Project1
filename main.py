
"""In Python, f-strings (or formatted string literals) are a way to embed expressions inside string literals. When
you put an f before the opening quote of a string literal, you can use curly braces {} to include expressions that
will be evaluated and inserted into the string."""


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


"""The code if __name__ == '__main__': is a common idiom used in Python modules to ensure that code is executed only 
when the module is run as the main program, and not when it is imported as a module by another program."""

if __name__ == '__main__':
    print_hi('PyCharm')