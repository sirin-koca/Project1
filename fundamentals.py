""" This is a comment
over many lines.
"""
# This is a short comment.
# Run this script in commandline e.g. Powershell by typing: py helloworld.py
# Let's learn Python!

# Print “Hello, World!” to console
print("Hello, World!")

y = "Hello, Sirin!"
print(y)

# Assigning variables:
x = 4  # x is of type int
x = "Sally"  # x is now of type string
print(x)
print(type(x))

# Get the name of the datatype with type() function:
x = 5
y = "John"
print(type(x))
print(type(y))

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

# Casting:
x = str(3)  # x will be '3'
y = int(3)  # y will be 3
z = float(3)  # z will be 3.0

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

# CASTING in Python
num = int(5.1)
msg = str(5)

# Mathematical operations
# Addition
x = 5
y = 3
result = x + y
print("The result of x + y is:", result)

# Subtraction
x = 5
y = 3
result = x - y
print("The result of x - y is:", result)

# Multiplication
x = 5
y = 3
result = x * y
print("The result of x * y is:", result)

# Division
x = 5
y = 3
result = x / y
print("The result of x / y is:", result)

# Integer division
x = 5
y = 3
result = x // y
print("The result of x // y is:", result)

# Modulus
x = 5
y = 3
result = x % y
print("The result of x % y is:", result)

# Exponentiation
x = 5
y = 3
result = x ** y
print("The result of x ** y is:", result)

# sirin-koca
