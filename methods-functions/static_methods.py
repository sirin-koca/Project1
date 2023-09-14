"""
Convert the instance method to a static method:
If the method doesn't need to access any instance-specific data or other
instance methods, you can make it a static method using the @staticmethod decorator:
"""
import sys


class MyClass:
    @staticmethod
    def instance_method():
        print("This is a static method.")


if __name__ == '__main__':
    sys.exit()
