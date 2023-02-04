import sys

# Python keywords

# and: logical operator that returns True if both operands are True, otherwise False.
print(True and False)  # returns False.

# as: used to create an alias for a module or to specify the context in which a class or function is used in a with
# statement. import math as m creates an alias m for the math module.

# assert: used to check if a given condition is True, and raises an AssertionError if the condition is False.
assert 2 + 2 == 4  # does not raise an error, but
try:
    assert 2 + 2 == 5  # raises an AssertionError.
except AssertionError:
    print("AssertionError raised")

# async: used to declare an asynchronous function that uses the asyncio library.
# async def my_async_func(): # declares an asynchronous function.


# await: used to pause execution of an asynchronous function until a result is returned from the function it is
# awaiting. await my_async_func() # pauses the execution of the current function until the result is returned from
# my_async_func().

# break: used to exit a loop prematurely.
for i in range(10):
    if i == 5:
        break  # stops the loop when `i` is equal to 5.

# class: used to define a new class in object-oriented programming.
# class MyClass: declares a new class called MyClass.

# continue: used to skip the current iteration of a loop and move on to the next iteration.
for i in range(10):
    if i % 2 == 0:
        continue  # skips over all even numbers.


# def: used to define a new function.
def my_func():  # declares a new function called my_func.
    pass


# del: used to delete an object, such as a list item or a variable.
my_var = 2
print(my_var)
del my_var  # deletes the variable my_var.

# elif: used in a conditional statement to check for additional conditions if the previous conditions were not met.
x = 3
if x < 0:
    print("Negative")
elif x == 0:
    print("Zero")
else:
    print("Positive")  # checks for negative, zero, and positive values of x.

if x >= 0:
    print("Non-negative")  # checks for negative and non-negative values of x.
# else: used in a conditional statement to specify the code to be executed if none of the conditions were met.
else:
    print("Negative")

# except: used to catch and handle exceptions that are raised in a try block.
try:
    x / 0
except ZeroDivisionError:
    print("Division by zero")  # catches a ZeroDivisionError and prints a message.

# False: boolean value that represents False.
# if 1 > 2 : print(1) #does not print anything.
# finally: used in a try-`

sys.exit()


