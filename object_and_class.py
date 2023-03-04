import sys

"""The __init__() method is a special method that is called when an object is created. It is also known as the 
constructor method. The main purpose of __init__() is to initialize the object's properties with the values passed in 
as arguments."""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# Create an object of the Person class
person1 = Person("Alice", 25)

# Call the say_hello() method on the object
person1.say_hello()

sys.exit()
