import datetime

# accessing the year attribute
today = datetime.datetime.now()
year = today.year
print("Current year:")
print(year)

birth_year = int(input("What is your birth year?"))
age = year - birth_year

print("Your age is:")
print(age)

exit()