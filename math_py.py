import math

a = 5
b = 4

if a >= b:
    c = a - b
else:
    c = b - a

print(a, b, c)


# Factorial function with user-input:
def fact_recursion(num):
    if num < 0:
        return -1
    if num == 0:
        return 1
    return num * fact_recursion(num - 1)


# takes user-input as integer
var = int(input("Type a number:"))

print(fact_recursion(var))

# built-in math-function for factorial:
print(math.factorial(6))

exit()
