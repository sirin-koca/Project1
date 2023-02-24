"""
"funkysirin" is the name of this interactive game. When you run the code, it first greets the user,
asks for their name and age, and then asks if they would like to play a game. If the user chooses to play,
they are asked to guess a random number between 1 and 100, and the program keeps track of how many tries it takes
the user to guess the correct number. If the user enters an invalid input,
a "ValueError" exception is raised and the user is prompted to enter a valid number.
"""
# Generate a random number with random-module
import random


# User interaction
def funkysirin():
    start = """Welcome! 
    Lets get to know you.
    Please identify yourself."""
    print(start)

    name = input("Whats your name?")
    age = input("How old are you?")
    if not name or not age:
        print("Who's there? Identify yourself or be gone, mysterious stranger!")
        exit()
    else:
        print("Your name and age is: " + name + ", " + age)
        print("*****Welcome " + name + "*****")

    choice = (input("Do you wanna play a game " + name + "? y / n ?"))

    if choice == "y":
        # Ask the user to guess the number
        print(":::Welcome to the number guessing game!:::")
        print("I'm thinking of a number between 1 and 100. Can you guess what it is?")
        number = random.randint(1, 100)
        count = 0
        while True:
            try:
                guess = int(input("Guess the number between 1 and 100: "))
                count += 1
                if guess > number:
                    print("Too high")
                elif guess < number:
                    print("Too low")
                else:
                    print("You got it! The number was", number)
                    # Print a message to the user indicating they won
                    print("Congratulations! You correctly guessed the number in", count, "tries.")
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

    elif choice == "n":
        print("Ok, have a good one!")
    else:
        print("Something went wrong, please try again!")


funkysirin()

exit()
