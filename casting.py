# In python, we cannot concatinate an int and a string together, so we need to use casting:

x = str(3)  # x will be '3'
y = int(3)  # y will be 3
z = float(3)  # z will be 3.0
num = int(5.1)
msg = str(5)
print("This is a number: ")
print(num)
print("This is a text: " + msg)

# User input is always a string, so we need to cast string to integer.
guess = int(input('Pick a number between 1 and 10: '))

exit()
