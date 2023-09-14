import sys

"""in Python, a module is a file that contains Python code. We can define functions, classes, and variables in a 
module, and then use them in other Python programs by importing the module. When we create a Python file, 
we are essentially creating a module. The name of the module is the name of the file ( without the .py extension)."""

import dog
import cat
import bird
import fish

"""The __name__ attribute is a special attribute that is automatically set by Python for each module. When a module 
is executed as the main program, its __name__ attribute is set to '__main__'. When a module is imported into another 
program, its __name__ attribute is set to the name of the module (i.e. the filename without the .py extension)."""

if __name__ == '__main__':
    print("Animals making noise:")
    dog.make_some_noise()
    cat.make_some_noise()
    bird.make_some_noise()
    fish.make_some_noise()

    print("\nAnimals eating food:")
    dog.my_food()
    cat.my_food()
    bird.my_food()
    fish.my_food()


def my_animals():
    animal = input("\n What's your favorite animal? ")
    if animal.isdigit():
        print("You must use letters")
    elif animal == 0:
        print("Use letters please!")
    elif animal == "dog":
        dog.make_some_noise()
        print("I love " + animal + " too!")
    elif animal == "cat":
        cat.make_some_noise()
    else:
        print("I love animals!")


my_animals()


sys.exit()
