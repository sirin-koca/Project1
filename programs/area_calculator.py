# Area Calculator 📏

import math
import sys

base = 20
height = 30
area = (base * height) / 2
print(f'The triangle area is {area}')  # Method1
# print("The triangle area is", area)  # Method2

length = 2
width = 12
area = length * width
print(f'The rectangle area is {area}')

radius = 36
area = round(math.pi * radius ** 2)
print(f'The circle area is {area}')

exit()
