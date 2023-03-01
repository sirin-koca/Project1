# Number Guessing Game

import random

# Create an empty list for attempts
attempts = []


def show_score():
    if not attempts:
        print('There is currently no high score, it\'s yours for the taking!')

    else:
        print(f'The current high score is {min(attempts)} attempts')


def start_game():
    attempts_count = 0
    rand_num = random.randint(1, 10)
    print('Hello traveler! Welcome to the game of guesses!')
    player_name = input('What is your name? ')
    wanna_play = input(
        f'Hi, {player_name}, would you like to play the guessing game?'
        '(Enter y/n): ')

    if wanna_play.lower() != 'y':
        print('That\'s cool, Thanks!')
        exit()
    else:
        show_score()

    while wanna_play.lower() == 'y':
        try:
            guess = int(input('Pick a number between 1 and 10: '))
            if guess < 1 or guess > 10:
                raise ValueError(
                    'Please guess a number within the given range')

            attempts_count += 1
            attempts.append(attempts_count)

            if guess == rand_num:
                print('Nice! You got it!')
                print(f'It took you {attempts_count} attempts')
                wanna_play = input(
                    'Would you like to play again? (Enter y/n): ')
                if wanna_play.lower() != 'y':
                    print('That\'s cool, have a good one!')
                    break
                else:
                    attempts_count = 0
                    rand_num = random.randint(1, 10)
                    show_score()
                    continue
            else:
                if guess > rand_num:
                    print('It\'s lower')
                elif guess < rand_num:
                    print('It\'s higher')

        except ValueError as err:
            print('Oh no!, that is not a valid value. Try again...')
            print(err)


if __name__ == '__main__':
    start_game()

    exit()
