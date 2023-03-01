# Number guessing program
import random

number = random.randint(1, 50)

# number_of_guesses = 0

for i in range(50):
    # while number_of_guesses < 50:
    print('Guess a number between 1 and 50:')
    guess = input()
    guess = int(guess)

    # number_of_guesses = number_of_guesses + 1

    if guess < number:
        print('Your guess is too low')

    if guess > number:
        print('Your guess is too high')

    if guess == number:
        break


if guess == number:
    print('Bravo! You guessed the number.')
else:
    print('You did not guess the number. The number was ' + str(number))


exit()
