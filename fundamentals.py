""" This is a comment
over many lines.
"""
# This is a short comment.

# Let's learn Python!
# Run this script in commandline like powershell by typing: py helloworld.py
# Remember to save the file after editing.
# The file (python script) has to be saved under "User" aka sirin.

print("# - Hello, World! What a beautiful day! Today we are going to learn PYTHON! :) ")

if 5 > 2:
    print("# - Yes, five is bigger than two")

y = "Hello, Sirin!"
print(y)

# ASSIGN and REASSIGN variables:
x = 4  # x is of type int
x = "Sally"  # x is now of type str
print(x)

# CASTING in Python:
x = str(3)  # x will be '3'
y = int(3)  # y will be 3
z = float(3)  # z will be 3.0

# Get the name of the datatype with type() function:
x = 5
y = "John"
print(type(x))
print(type(y))

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
