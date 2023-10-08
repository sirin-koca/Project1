# Python Fundamentals
An introduction to the most fundamental aspects of Python programming language.
My Python projects: [Programs](https://github.com/sirin-koca/Python_Fundamentals/tree/master/programs)

---

## Introduction
Python is a high-level, interpreted, and general-purpose programming language that is easy to learn and has a simple syntax. It is a versatile language and can be used for a wide range of applications, such as web development, data analysis, machine learning, and artificial intelligence. Its simplicity and ease of use, combined with its extensive libraries and frameworks, make it a go-to language for a variety of technical tasks. Whether you're building machine learning models, automating workflows, or developing web applications, Python is a language that can handle it all with grace and ease. Python has also a vast library of modules and packages that make it easier to accomplish complex tasks with minimal coding.

Some of the key features of Python are:

- Interpreted language
- Object-oriented
- Dynamically typed
- Cross-platform

## Data Types
Python supports several data types, including:
Numbers (int, float, complex),
Strings,
Lists,
Tuples,
Sets,
Dictionaries,
Boolean. 
Understanding data types is important as it allows you to work with data effectively and manipulate it to achieve your desired results.

## Variables
Variables are used to store data in a program. In Python, variables are dynamically typed, meaning you do not need to declare the type of a variable explicitly. To assign a value to a variable, you can use the equal (=) operator.

```
x = 10
y = "Hello World"
```

## Control Flow / If-Statements
Control flow statements are used to control the flow of a program. Python supports the following control flow statements:
if...else statements,
for loops,
while loops,
break and continue statements. 
These statements allow you to write programs that can make decisions and repeat tasks based on certain conditions.

## Functions
Functions are blocks of code that can be reused multiple times in a program. They allow you to write modular and reusable code, which can save you a lot of time and effort. To define a function, you use the def keyword followed by the function name and parameters.

```
def add_numbers(x, y):
    return x + y
```

## Classes
Classes are used to define objects in Python. They allow you to encapsulate data and behavior into a single unit, making it easier to work with complex data structures. To define a class, you use the class keyword followed by the class name.

```
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
```

## Modules
Modules are files that contain Python code. They allow you to organize your code into logical units, making it easier to manage and reuse. Python comes with a large number of built-in modules, and you can also create your own modules.

```
import math
print(math.pi)
```

Here are some examples of popular Python modules:

* __os module__: Provides a way to interact with the operating system, including tasks such as file and directory operations, process management, and user and group management.

* __sys module__: Provides access to system-specific parameters and functions, such as the command line arguments, the standard input and output streams, and the Python interpreter's version information.

* __math module__: Provides mathematical functions and constants, such as trigonometric functions, logarithmic functions, and the value of pi.

* __datetime module__: Provides classes for working with dates, times, and time intervals, including functions for formatting and parsing dates and times.

* __random module__: Provides functions for generating random numbers, shuffling sequences, and selecting random elements from a sequence.

* __re module__: Provides regular expression matching operations, allowing you to search for and manipulate text using patterns.

* __json module__: Provides functions for encoding and decoding JSON data, which is a lightweight data format used for exchanging data between applications.

* __requests module__: Provides functions for making HTTP requests, allowing you to interact with web APIs and retrieve data from the internet.

* __numpy module__: Provides fast, efficient arrays for numerical computing, allowing you to perform complex calculations on large datasets.

* __pandas module__: Provides data analysis and manipulation tools, allowing you to work with structured data such as spreadsheets and SQL tables.


## File Handling
File handling is the process of reading from and writing to files on your computer. Python provides several functions for file handling, including open(), read(), write(), and close(). Understanding file handling is important for working with data stored in files.

## Conclusion
Python is a powerful and versatile language that is easy to learn and use. Understanding the fundamentals of Python, such as data types, variables, control flow statements, functions, classes, modules, and file handling, can help you become a more effective programmer.

---

<table> 
<thead>
<tr>
<th>Variables</th>
<th>Control flow</th>
<th>Functions</th>
</tr>
</thead>
<tbody>
<tr>
<td td valign="top"> Variables in Python are created on the fly by assigning a value to a name. They are dynamically typed, which means that the type of a variable can change based on the value assigned to it.


```
# Variable assignment:
x = 5

# x is now 10
x = 10      
y = "Hello" 
name = "Sirin"

# Arithmetic operations:
y = 2
print(x + y)  # 7
print(x - y)  # 3

# Casting:
x = str(3)  # x will be '3'
y = int(3)  # y will be 3
z = float(3)  # z will be 3.0
num = int(5.1)
```

</td>
<td td valign="top"> Python provides a variety of control flow statements such as conditional statements for branching and looping. The if statement is used to test a condition and execute a block of code if the condition is <code/>True</code>. An else clause can be used to execute a block of code if the condition is <code>False</code>.   


```
if x > 0:
print("x is positive")
else:
print("x is not positive")    
```

For loops: 
The for loop is used to iterate over a sequence (such as a list or a string).

```
for i in range(10):
print(i)  
```

While loops: 
The while loop is used to execute a block of code as long as a condition is true.

```
i = 0
while i < 10:
print(i)
i += 1
```

</td>
<td td valign="top"> Functions in Python are defined using the <code>def</code> keyword. They can take any number of arguments, and can return a value.  


```
# Function definition:
def factorial(n):
if n == 0:
return 1
else:
return n * factorial(n-1)

# Function definition:
def add_numbers(x, y):
    return x + y

# Function call:
result = add_numbers(5, 3)
print(result)  # Output: 8
``` 

</td>
</tr>        
</tbody>
</table>

[sirin-koca](https://github.com/sirin-koca) | OsloMet 2022
