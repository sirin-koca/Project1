"""
isinstance is a built-in function in Python that allows you to check if an object is an instance of a specified class
or of a subclass thereof. The function takes two arguments: the object and the class. If the object is an instance of
the class or a subclass, isinstance returns True, otherwise it returns False. For example:

x = 5
    isinstance(x, int)
Output: True
    isinstance(x, float)
Output: False

In the example, x is an instance of the int class, so isinstance(x, int) returns True.
"""

# BASIC FUNCTIONS in PYTHON:
# print() - used to display output on the screen. For example:
print("Hello, World!")

# len() - returns the length of a sequence (such as a string, list, or tuple). For example:
name = "John Doe"
print(len(name))  # prints 8

# type() - returns the type of object. For example:
num = 42
print(type(num))  # prints <class 'int'>

# int() - converts a value to an integer. For example:
float_num = 3.14
print(int(float_num))  # prints 3

# float() - converts a value to a floating-point number. For example:
int_num = 3
print(float(int_num))  # prints 3.0

# str() - converts a value to a string. For example:
num = 42
print(str(num))  # prints '42'

# sum() - returns the sum of elements in an iterable (such as a list or tuple). For example:
numbers = [1, 2, 3, 4]
print(sum(numbers))  # prints 10

# min() - returns the minimum value in an iterable. For example:
numbers = [1, 2, 3, 4]
print(min(numbers))  # prints 1

# max() - returns the maximum value in an iterable. For example:
numbers = [1, 2, 3, 4]
print(max(numbers))  # prints 4

# sorted() - returns a sorted list from an iterable. For example:
numbers = [3, 1, 4, 2]
print(sorted(numbers))  # prints [1, 2, 3, 4]

# split()
""" The split() method is a built-in method in Python for strings. It splits a string into a list of substrings based on 
a specified delimiter, which by default is any whitespace character (such as a space, tab, or line break).
"""
text = "This is a sample text"
words = text.split()
print(words)  # prints ['This', 'is', 'a', 'sample', 'text']


# isinstance function:

# Example1
def is_integer(x):
    if isinstance(x, int):
        return True
    else:
        return False


# Check if the input is an integer or not
print(is_integer(3))  # True
print(is_integer(3.5))  # False


# Example2
def add_numbers(x, y):
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        return x + y
    else:
        raise ValueError("Inputs must be numbers (int or float)")


# Add two numbers
print(add_numbers(3, 4))  # outputs 7


# Example3
def is_list_of_integers(lst):
    if all(isinstance(x, int) for x in lst):
        return True
    else:
        return False


# Check if the input is a list of integers
print(is_list_of_integers([1, 2, 3, 4]))  # True
print(is_list_of_integers([1, 2, 3, 4.5]))  # False

exit()
