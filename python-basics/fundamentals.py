""" This is a comment
over many lines.
"""
import sys

# This is a short comment.
# Run this script in commandline e.g. Powershell by typing: py helloworld.py
# Let's learn Python!

# Print “Hello, World!” to console
print("Hello, World!")

y = "Hello, Sirin!"
print(y)

# Assigning variables:
x = 4  # x is of type int
xs = "Sally"  # x is now of type string
print(x)
print(type(xs))

# Get the name of the datatype with type() function:
xnum = 5
ystring = "John"
print(type(xnum))
print(type(ystring))

# Conditional statements:
if 5 > 2:
    print("# - Yes, five is bigger than two")

x = 5
if x > 0:
    print("x is positive")
else:
    print("x is negative")

x = 5
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

x = "John"
# is the same as
x = 'John'

""" 
Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
"""
myVariableName = "John"
MyVariableName = "John"
my_variable_name = "John"

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

# UNPACK a list
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python is cool!"
print(x)

# Casting:
x = str(3)  # x will be '3'
y = int(3)  # y will be 3
z = float(3)  # z will be 3.0
num = int(5.1)
msg = str(5)
print("This is a number: ")
print(num)
print("This is a text: " + msg)

# Mathematical operations
# Addition
a = 5
b = 3
result = a + b
print("The result of x + y is:", result)

# Subtraction
x1 = 5
y1 = 3
result = x1 - y1
print("The result of x - y is:", result)

# Multiplication
x2 = 5
y2 = 3
result = x2 * y2
print("The result of x * y is:", result)

# Division
x3 = 5
y3 = 3
result = x3 / y3
print("The result of x / y is:", result)

# Integer division
x4 = 5
y4 = 3
result = x4 // y4
print("The result of x // y is:", result)

# Modulus
x5 = 5
y5 = 3
result = x5 % y5
print("The result of x % y is:", result)

# Exponentiation
x6 = 5
y6 = 3
result = x6 ** y6
print("The result of x ** y is:", result)

sys.exit()
# sirin-koca
