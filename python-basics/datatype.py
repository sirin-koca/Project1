import sys

datatype = "Sirin"
print("My datatype is: ", type(datatype))

x = 1
hi = "Hello there"
name = "Sirin"
print(hi + " " + name)

try:
    print(hi + " " + name + str(x))
except Exception as e:
    print("Error:", e)
finally:
    print("Convert numbers to a string before concatenation.")

x = 2
print(x)

x_str = str(x)  # converted to string

print("my fav num is", x, ".", "x =", x)  # Using commas to separate values
print("my fav num is " + x_str + ".", x_str)  # Using plus to concatenate

sys.exit()
