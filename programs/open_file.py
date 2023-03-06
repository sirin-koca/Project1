# We will use the os-module:
import os
import sys

# Show current directory:
cwd = os.getcwd()
ls = os.listdir()

print("Current working directory:", cwd)
print("Items in this directory:", ls)

# Get user input to open a file from this directory:
name = input("Enter file name: ")


def open_file():
    try:
        my_file = open(name)
        return my_file
    except FileNotFoundError:
        return None


file = open_file()
if file:
    # do something with the file here
    print("File opened successfully")
    os.startfile(name)
else:
    print("File not found")

sys.exit()
