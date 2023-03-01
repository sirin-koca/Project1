# Basic calculator

print("Welcome to the calculator!")

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter an operator (+, -, *, /): ")

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        print("Invalid operator.")
        result = None

    if result is not None:
        print("Result:", result)

except ValueError:
    print("Invalid input: not a number.")

"""
We can also create methods for each operation:
def add(x, y):
    return x + y


def multip(x, y):
    return x * y
"""

exit()
