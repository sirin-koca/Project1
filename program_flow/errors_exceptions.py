"""Python refers to the mistakes within the program as errors and will point to the location where an error occurred
with a ^ character. When programs throw errors that we didn’t expect to encounter, we call those errors bugs.
Programmers call the process of updating the program so that it no longer produces bugs debugging.

Two common errors that we encounter while writing Python are SyntaxError and NameError.

SyntaxError means there is something wrong with the way your program is written — punctuation that does not belong,
a command where it is not expected, or a missing parenthesis can all trigger a SyntaxError.

A NameError occurs when the Python interpreter sees a word it does not recognize. Code that contains something that
looks like a variable but was never defined will throw a NameError.
"""

# NameError
print("This is a message")
# print(Abracadabra) throws a NameError: name 'Abracadabra' is not defined

"""
In Python, exceptions are events that occur during the execution of a program that disrupt
the normal flow of execution. There are several built-in exceptions in Python, including:

1- ValueError: Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value.
2- TypeError: Raised when an operation or function is applied to an object of inappropriate type.
3- ZeroDivisionError: Raised when division or modulo by zero takes place for all numeric types.
4- NameError: Raised when a local or global name is not found.
5- FileNotFoundError: Raised when a file or directory is requested but doesn't exist.
6- KeyError: Raised when a dictionary key is not found in the set of existing keys.
7- IndexError: Raised when an index is not found in a sequence.
8- MemoryError: Raised when an operation runs out of memory.

Exception handling in Python is done using the try and except statements. The basic syntax is:
"""

# Example1: ValueError
# type a letter when u r asked to type a nr to activate exception handling
try:
    x = int(input("Enter a number: "))
except ValueError:
    print("Oops!  That was no valid number. Try again!")


# Example2: FileNotFoundError
f = None
try:
    f = open("test.txt", "r")
    contents = f.read()
    print(contents)
except FileNotFoundError:
    print("File not found.")
finally:
    if f:
        f.close()
        print("File closed.")

# Example3:
value = input("Enter a number: ")

try:
    number = int(value)
    if number > 0:
        print("The number is positive.")
    else:
        print("The number is non-positive.")
except ValueError:
    print("Invalid input: not a number.")


exit()
