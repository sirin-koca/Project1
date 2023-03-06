# Import os-module:
import os

# Show current directory and its items:
cwd = os.getcwd()
ls = os.listdir()

print("Current working directory:", cwd)
print("Items in this directory:", ls)

# Get user input for file name to open:
name = input("Enter file name: ")


def sirin():
    try:
        my_file = open(name)
        return my_file
    except FileNotFoundError:
        return None


file = sirin()
if file:
    # do something with the file here
    print("File opened successfully")
    content = file.read()
    print(content)
else:
    print("File not found")

