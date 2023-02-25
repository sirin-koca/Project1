"""
Logical-statements:
In Python we have 3 logical statements (like in discrete mathematics): and, or, not.
    and: returns true if both are true,
    or: returns true at least one of its true,
    not: inverts the given truth value.

If-statements: 
An "if statement" is written by using the "if" keyword. 
Python supports the usual logical conditions from mathematics:
    Equals: a == b
    Not Equals: a != b
    Less than: a < b
    Less than or equal to: a <= b
    Greater than: a > b
    Greater than or equal to: a >= b
    These conditions can be used in several ways, most commonly in "if statements" and loops.

Indentation:
Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. 
Other programming languages often use curly-brackets for this purpose.
"""

if 'Yes' == 'Yes':
    # evaluates to True
    print('They are equal')

if (2 > 1) == (5 < 10):
    # evaluates to True
    print('Both expressions give the same result')
c = '2'
d = 2

if c == d:
    print('They are equal')
else:
    print('They are NOT equal')

# Not Equals Operator
if "Yes" != "No":
    # evaluates to True
    print("They are NOT equal")

val1 = 10
val2 = 20

if val1 != val2:
    print("They are NOT equal")

if (10 > 1) != (10 > 1000):
    # True != False
    print("They are NOT equal")

# if Statement -----------------------------------------------------

test_value = 100

if test_value > 1:
    # Expression evaluates to True
    print("This code is executed!")

if test_value > 1000:
    # Expression evaluates to False
    print("This code is NOT executed!")

    print("Program continues at this point.")

# elif Statement ---------------------------------------------------------

pet_type: str = "fish"

if pet_type == "dog":
    print("You have a dog.")
elif pet_type == "cat":
    print("You have a cat.")
elif pet_type == "bird":
    # this is performed
    print("You have a" + pet_type)
else:
    print("Not sure!")

# else Statement --------------------------------------------------------------

test_value = 50

if test_value < 1:
    print("Value is < 1")
else:
    print("Value is >= 1")

test_string = "VALID"

if test_string == "NOT_VALID":
    print("String equals: NOT_VALID")
else:
    print("String equals: VALID")

exit()
