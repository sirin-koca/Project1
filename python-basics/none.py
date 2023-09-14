"""
None in Python is similar to null in Java.

Both None and null represent the absence of a value. In both Python and Java,
you can use these values to indicate that a variable doesn't contain a meaningful value.

However, this rule applies only Python:
The default return value of a function that doesn't explicitly return anything is None.

In Java there is no such thing as default return value of a function. Functions must either
have a return type or use the keyword "void", in which case it does not return any value.
"""
import sys


def my_function(arg=None):
    if arg is None:
        print("No argument was passed to the function.")
    else:
        print("The argument is:", arg)


my_function()  # Output: No argument was passed to the function.
my_function("hello")  # Output: The argument is: hello


def funkysirin(name=None, age=None):
    if name is None:
        name = input("Whats your name?")
    if age is None:
        age = input("How old are you?")
    if not name and not age:
        print("Who are you?")
    else:
        print("My name and age: " + name, age)


funkysirin()

sys.exit()
