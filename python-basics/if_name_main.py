#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The if __name__ == '__main__': idiom is a powerful and elegant solution in Python that allows a single script to
serve dual purposes:

As a Standalone Program: When you run the script directly, the "main script execution code" inside the if __name__ ==
'__main__': block gets executed. This is useful for testing, demonstrating the functionality of the script,
or when the script is intended to be a standalone application.

As a Module: When you import the script into another script or module, only the function and class definitions (and
other top-level code) are available, and the "main script execution code" doesn't run. This allows the script to
provide reusable functions, classes, and other resources to other scripts without executing the main logic.

This design pattern promotes code reusability and modularity. By organizing your code this way, you can build
data_extraction of functions and classes that can be easily imported and used in multiple projects, while still being able
to run and test each script individually. It's one of the many features that make Python a versatile and
developer-friendly language."""

import sys

"""When a script is imported as a module: Only the function and class definitions (and any other top-level code) will 
be executed. The code inside the if __name__ == '__main__': block will not run."""


# Execute this when imported as a module:
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


# Execute this when runned as standalone program:
if __name__ == '__main__':
    x = 10
    y = 5
    print(f"{x} + {y} = {add(x, y)}")
    print(f"{x} - {y} = {subtract(x, y)}")

    sys.exit()
