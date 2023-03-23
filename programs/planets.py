from datetime import date
date.today()
print(date.today())
print(date.today().year)
print(date.today().month)
print(date.today().day)

# variables
planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367 # float, lightyears
can_liftoff = True # boolean
shuttle_landed_on_the_moon = "Apollo 11" #string
distance_to_alpha_centauri = 4.367 # looks like a float

# printing the type of the variables
type(distance_to_alpha_centauri) ## <class 'float'>
print(type(distance_to_alpha_centauri))
print(type(shuttle_landed_on_the_moon))
print(type(can_liftoff))
print(type(planets_in_solar_system))

print(type(date.today()))
print(type(date.today().year))
print(type(date.today().month))
print(type(date.today().day))
