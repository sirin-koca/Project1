"""In Python, self is a convention used to refer to the instance of a class. When you define a method in a class,
the first parameter of the method is usually self, which refers to the instance of the class that the method is being
called on.

In this example, we define a Car class with an __init__ method that takes two parameters, make and model,
as well as the self parameter. Inside the __init__ method, we set two instance variables (self.make and self.model)
to the values of the make and model parameters.

We also define a drive method that takes one parameter, self, which allows us to access the instance variables of the
Car class. Inside the drive method, we print out a message that includes the values of self.make and self.model.

Finally, we create an instance of the Car class (car1) with the make "Toyota" and model "Corolla". We then call the
drive method on car1, which prints out the message "The Toyota Corolla is driving."""
import sys


# Example
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        print("The {} {} is driving.".format(self.make, self.model))


car1 = Car("Toyota", "Corolla")
car1.drive()  # output: The Toyota Corolla is driving.

sys.exit()