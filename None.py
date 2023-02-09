"""
None in Python is similar to null in Java. Both None and null represent the absence of a value.
In both Python and Java, you can use these values to indicate that a variable doesn't contain a meaningful value,
or to represent the default value for a function that doesn't return anything.
"""


def my_function(arg=None):
    if arg is None:
        print("No argument was passed to the function.")
    else:
        print("The argument is:", arg)


my_function()  # Output: No argument was passed to the function.
my_function("hello")  # Output: The argument is: hello

exit()

