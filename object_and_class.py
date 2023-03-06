import sys

# __init__
"""The __init__() method is a special method that is called when an object is created. It is also known as the 
constructor method. The main purpose of __init__() is to initialize the object's properties with the values passed in 
as arguments."""

# self
"""In Python, self is a convention used to refer to the instance of a class. When you define a method in a class,
the first parameter of the method is usually self, which refers to the instance of the class that the method is being
called on.

When creating a new object, Python automatically passes the object itself as the first argument to the __init__() 
method, which is traditionally named self."""


# Let's create a class called Person:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

        """The self parameter is used to refer to the object that is being created, and is passed in automatically by 
        Python. We can then use self to access the object's properties and methods, like self.name and self.age."""


# Create an object of the Person class
person1 = Person("Alice", 25)

# Call the say_hello() method on the object
person1.say_hello()


# Another class: Animal
class Animal:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def voice(self):
        print(f"Hello, my name is {self.name} and I am a {self.breed}.")


# Create an object of the Animal class
animal1 = Animal("Maya", "dog")

# Call the method of this class
animal1.voice()

sys.exit()
