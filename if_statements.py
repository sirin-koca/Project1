# If-statements

# ex1
test_value = 100

if test_value > 1:
    print("This code is executed!")

if test_value > 1000:
    print("This code is NOT executed!")

print("Program continues at this point.")
print("*" * 10)

# ex2
pet = "dog"

if pet == "dog":
    print("You have a dog!")
elif pet == "cat":
    print("You have a cat!")
elif pet == "fish":
    print("You have a fish!")
else:
    print("You dont have a pet!")

name = input("Whats the name of your dog?")
print("My dogs name is " + name)
print("*" * 10)

# ex3
uname = input("Hello, what is your name?")
if uname == "Dave":
    print("Get off my computer Dave!")

is_raining = True
if is_raining:
    print("It is going to rain today. Bring an umbrella! ")

exit()
