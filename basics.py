# Python basics!
# Comment on a single line
user = "JDoe"  # Comment after code

# Arithmetic operations
result1 = 10 + 30
result2 = 40 - 10
result3 = 50 * 5
result4 = 16 / 4
result5 = 25 % 2
result6 = 5 ** 3
print(result1, result2, result3, result4, result5, result6)

# Concatenation
"""
In Python, you cannot concatenate a string and an integer directly because they have different data types. 
We need to convert the integer to a string first. You can do this by using the str() function to convert 
the integer to a string, and then you can concatenate the two values. Here is an example:
"""
x = 42
y = "The answer is: "
z = y + str(x)
print(z)

# Plus-Equal Operator

counter = 0
counter += 10

# This is equivalent to

counter = 0
counter = counter + 10

# The operator will also perform string concatenation

message = "Part 1 of message "
message += "Part 2 of message"

# These are all valid variable names and assignment

user_name = "codey"
user_id = 100
verified = False

# A variable's value can be changed after assignment

points = 100
points = 120

# Modulo operations

zero = 8 % 4

nonzero = 12 % 5

# Example integer numbers

chairs = 4
tables = 1
broken_chairs = -2
sofas = 0

# Non-integer numbers

lights = 2.5
left_overs = 0.0

# String concatenation

first = "Hello "
second = "World"

result = first + second

long_result = first + second + "!"

numerator = 100
denominator = 0
# bad_results = numerator / denominator  # ZeroDivisionError: division by zero

user = "User Full Name"
game = 'Monopoly'

longer = "This string is broken up \
over multiple lines"

# SyntaxError: can't assign to operator
# age = 7 + 5 = 4


print("Hello World!")

print(100)

# Floating point numbers

pi = 3.14159
meal_cost = 12.99
tip_percent = 0.20

pi = 3.14159
print(pi)

# LIST
primes = [2, 3, 5, 7, 11]
print(primes)

empty_list = []

items = ['cake', 'cookie', 'bread']
total_items = items + ['biscuit', 'tart']
print(total_items)
# Result: ['cake', 'cookie', 'bread', 'biscuit', 'tart']

numbers = [1, 2, 3, 4, 10]
names = ['Jenny', 'Sam', 'Alexis']
mixed = ['Jenny', 1, 2]
list_of_lists = [['a', 1], ['b', 2]]

orders = ['daisies', 'periwinkle', 'tulips']
print(orders)
# Result: ['daisies', 'periwinkle', 'tulips']

soups = ['minestrone', 'lentil', 'pho', 'laksa']
print(soups[-1])  # 'laksa'
print(soups[-3:])  # 'lentil', 'pho', 'laksa'
print(soups[:-2])  # 'minestrone', 'lentil'

exit()
