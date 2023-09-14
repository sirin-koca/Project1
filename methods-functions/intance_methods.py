"""
INSTANCE METHODS in CLASSES:

In instance methods of a class, the first argument is a reference to the instance of the object itself.

By convention, this argument is named self. It's automatically passed by Python when you call
an instance method on an object.

"""
import sys


class MyClass:
    def instance_method(self) -> None:
        print("This is an instance method using: ", self)


# When you call this method:

obj = MyClass()
obj.instance_method()  # You don't pass 'self', Python does it.
# Here, obj.instance_method() is equivalent to MyClass.instance_method(obj).

sys.exit()