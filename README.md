# Python
Python is a high-level, interpreted programming language that is both versatile and powerful. Its simplicity and ease of use, combined with its extensive libraries and frameworks, make it a go-to language for a variety of technical tasks. Whether you're building machine learning models, automating workflows, or developing web applications, Python is a language that can handle it all with grace and ease.

My Python projects: [Programs](https://github.com/sirin-koca/Python_Fundamentals/tree/master/programs)

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
<td td valign="top"> Python provides a variety of control flow statements such as conditional statements for branching and looping. The if statement is used to test a condition and execute a block of code if the condition is true. An else clause can be used to execute a block of code if the condition is false.   


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

[sirin-koca](https://github.com/sirin-koca) | OsloMet 2023
