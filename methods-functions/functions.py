"""Functions in Python:
In Python, you can define a function using the def keyword, followed by the name of the
function, and then a set of parentheses that may or may not include parameters (input values) that the function
expects to receive.

If you want your function to return a value, you can use the return keyword followed by the value you want to return.

_isinstance_ is a built-in function in Python that allows you to check if an object is an instance of a specified class
or of a subclass thereof. The function takes two arguments: the object and the class. If the object is an instance of
the class or a subclass, isinstance returns True, otherwise it returns False. For example:

x = 5
    isinstance(x, int)
Output: True
    isinstance(x, float)
Output: False

In the example, x is an instance of the int class, so isinstance(x, int) returns True.
"""
import sys


# Function definition in Python: how to define our own functions / methods:
# How to use BUILT-IN Functions:


def hello_world1():
    msg = "It's a beautiful day!"
    print("Hello world! " + msg)


# Function call:
hello_world1()


def hello_world2(myname):
    print("My name is " + myname)


# Function call:
hello_world2("Alexander The Great!")

# Parameters: These are the inputs that you pass to the function.
# You can define a function to take zero or more parameters. For example:

uname = input("Please enter your name:")


def greet():
    print(f"Hello, {uname}!")


greet()


# isinstance
def is_integer(x):
    if isinstance(x, int):
        return True
    else:
        return False


# Function call: is_integer
# This function checks if the input is an integer or not
print(is_integer(3))  # True
print(is_integer(3.5))  # False


def add_numbers(x, y):
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        return x + y
    else:
        raise ValueError("Inputs must be numbers (int or float)")


def is_list_of_integers(lst):
    if all(isinstance(x, int) for x in lst):
        return True
    else:
        return False


# Function call: add_numbers
print(add_numbers(3, 4))  # outputs 7

# Function call: is_list_of_integers
# This function checks if the input is a list of integers
print(is_list_of_integers([1, 2, 3, 4]))  # True
print(is_list_of_integers([1, 2, 3, 4.5]))  # False

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
""" 
The split() method is a built-in method in Python for strings. It splits a string into a list of substrings based on 
a specified delimiter, which by default is any whitespace character (such as a space, tab, or line break).
"""
text = "This is a sample text"
words = text.split()
print(words)  # prints ['This', 'is', 'a', 'sample', 'text']

sys.exit(0)
