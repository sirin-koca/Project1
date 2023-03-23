# Path: programs\user_input.py
print("Welcome to the greeter program")
name = input("Enter your name: ")
print("Greetings " + name + "!")

print("Welcome to the calculator program. \n Please enter two numbers to add them together.")
first_number = input("first number: ")
second_number = input("second number: ")
print("The result is: " + str(int(first_number) + int(second_number)))

parsecs_input = input("Input number of parsecs:")
parsecs = int(parsecs_input)
lightyears = 3.26156 * parsecs

print(parsecs_input + " parsecs is " + str(lightyears) + " lightyears")

print("Have a nice day!")


SystemExit
