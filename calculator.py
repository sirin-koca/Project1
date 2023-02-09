def add(x, y):
    return x + y


def multip(x, y):
    return x * y


print("Welcome to the calculator!")
num1 = int(input("Type the first number:"))
num2 = int(input("Type the second number:"))

print("What do you want to do with these numbers?")
print("1. Add")
print("2. Multiply")

choice = int(input("Enter your choice (1 or 2): "))

"""
# Alternative1
if choice == 1:
    print(num1+num2)
elif choice == 2:
    print(num1*num2)
else:
    print("Something went wrong, please try again!")
    result = None
"""

# Alternative2
if choice == 1:
    result = add(num1, num2)
elif choice == 2:
    result = multip(num1, num2)
else:
    print("Invalid choice")
    result = None

if result is not None:
    print("The result is:", result)

exit()
