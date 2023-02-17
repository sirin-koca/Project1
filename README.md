# Python
Python is a high-level, interpreted programming language that is both versatile and powerful. Its simplicity and ease of use, combined with its extensive libraries and frameworks, make it a go-to language for a variety of technical tasks. Whether you're building machine learning models, automating workflows, or developing web applications, Python is a language that can handle it all with grace and ease.

### Variables
Variables in Python are created on the fly by assigning a value to a name. They are dynamically typed, which means that the type of a variable can change based on the value assigned to it.
```
# variable assignment
x = 5
x = 10      # x is now 10
y = "Hello" # Assigns the string value "Hello" to the variable y
name = "Sirin"
```

### Control Flow: conditional / if-else statements
Python provides a variety of control flow statements for branching and looping. The if statement is used to test a condition and execute a block of code if the condition is true. An else clause can be used to execute a block of code if the condition is false.

```
if x > 0:
    print("x is positive")
else:
    print("x is not positive")    
```

### Loops
Python provides two types of loops: for loops and while loops.

#### For loops:
The for loop is used to iterate over a sequence (such as a list or a string).

```` 
for i in range(10):
    print(i)    
```` 

#### While loops: 
The while loop is used to execute a block of code as long as a condition is true.

````
i = 0
while i < 10:
    print(i)
    i += 1
````

## Functions
Functions in Python are defined using the def keyword. They can take any number of arguments, and can return a value.
````
def add_numbers(x, y):
    return x + y

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
```` 
This function factorial() uses recursion to calculate the factorial of a number. If the input n is zero, it returns 1 (since 0! is defined as 1). Otherwise, it multiplies n by the result of calling the factorial function recursively with n-1 as the argument.

###  Examples
```
# arithmetic operations
y = 2
print(x + y)  # 7
print(x - y)  # 3

# conditional statement
if x > 0:
    print("x is positive")
else:
    print("x is negative")

# function definition
def add(a, b):
    return a + b

# function call
result = add(x, y)
print(result)  # outputs 7 : (5 + 2)

# import statement
import math
print(math.pi)  # 3.141592653589793

```

[sirin-koca](https://github.com/sirin-koca) | OsloMet 2023
