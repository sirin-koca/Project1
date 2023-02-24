# Building a project with Python from scratch.

import random
import sys

"""Information about this project: 
This is a simple spinning game, a Slot Machine with letters. User is asked how much they want to bet on which lines. 
There are maximum 3 lines with 3 columns matrix with letters A, B, C, D. At the end of each game, user is informed 
if they won, current balance and if they want to continue to play or quit.
The price for winnings: "A": 5, "B": 4, "C": 3, "D": 2. 
"""

# These variables are final / constant so that we can use anywhere in our program
MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbols_count in symbols.items():
        for _ in range(symbols_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]  # we make a copy
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end=" \n")


# Collecting user input as deposits
def deposit():
    while True:  # we need to ask the user give a deposit amount until they give a valid amount
        amount = input("What would you like to deposit? $:")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero.")
        else:
            print("Please enter a number.")
    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter max.nr. lines to bet on (1-" + str(MAX_LINES) + ")?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $:")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount


def game(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You dont have enough cash. Your current balance is ${balance}.")
            sys.exit()
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Your total bet is: ${total_bet}.")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_count)
    print(f"You won ${winnings}.")
    print(f"You won on line: ", *winning_lines)

    return winnings - total_bet


def main():
    # We call our function to collect user input
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        spin = input("Press enter to play (q to quit).")
        if spin == "q":
            break
        balance += game(balance)

    print(f"You left ${balance}")


main()

sys.exit()
