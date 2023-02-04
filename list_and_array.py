"""
The main differences between lists and arrays in Python:
# Definition: Lists are defined using square brackets, whereas arrays are defined using the array module.
# Element Type: Lists can store elements of different types, whereas arrays can store only elements of a single, specified type.
# Memory Efficiency: Arrays are more memory-efficient than lists, as they store elements using a compact representation.
# Performance: Arrays are faster than lists when it comes to specific operations like indexing, iteration, and slicing.
# Built-in Methods: Lists have a lot of built-in methods for manipulating elements and data, whereas arrays have fewer built-in methods.
# Use Cases: Lists are more flexible and can be used in a wide range of use cases, whereas arrays are more suited to numerical computations or when memory efficiency is a concern.

OBS!
Lists and arrays are not the same thing in Python.
A list is a built-in data structure in Python that is used to store an ordered collection of items,
which can be of any type (strings, integers, etc.). Lists are defined using square brackets,with each item separated by a comma:
"""

import array
import sys

# LISTS in PYTHON:

# Creating a list
fruits = ["apple", "banana", "cherry"]
my_list = [1, 2, 3, "hello"]
print(my_list)
print(fruits)

# Accessing elements in a list
print(fruits[0])  # Output: "apple"
print(my_list[2]) # Output: 3

# Modifying elements in a list
fruits[1] = "pear"
print(fruits)  # Output: ["apple", "pear", "cherry"]

# Adding elements to a list we use "append" keyword to add an item at the of a list
fruits.append("orange")
print(fruits)  # Output: ["apple", "pear", "cherry", "orange"]

# Removing elements from a list
fruits.remove("pear")
print(fruits)  # Output: ["apple", "cherry", "orange"]

# Sorting a list
fruits.sort()
print(fruits)  # Output: ["apple", "cherry", "orange"]

# Getting the length of a list, we use the keyword "len"
print(len(fruits))  # Output: 3

# A list comprehension to square the numbers in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# ARRAYS in PYTHON
my_array = array.array("i", [1, 2, 3, 4, 5])  # creates an array of integers.

sys.exit()
