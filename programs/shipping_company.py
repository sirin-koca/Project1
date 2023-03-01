# Shipping Company

"""
In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship it.

Options for a customer to ship their package:

1- Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
2- Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
3- Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.

Ground Shipping Rates:

Weight of Package	                  Price per Pound	    Flat Charge
2 lb or less	                      $1.50	                $20.00
Over 2 lb but less / equal to 6 lb	  $3.00	                $20.00
Over 6 lb but less / equal to 10 lb	  $4.00	                $20.00
Over 10 lb	                          $4.75	                $20.00

Now we will ceate an if/elif/else statement for the cost of ground shipping. It should check for weight, and print
the cost of shipping a package of that weight.
"""


# Ground Shipping:
def ground_shipping():
    weight = float(input("How much does your package weight?"))
    if weight <= 2:
        cost = weight * 1.50 + 20
        print(cost)
    elif 2 < weight <= 6:
        cost = weight * 3 + 20
        print(cost)
    elif 6 < weight <= 10:
        cost = weight * 4 + 20
        print(cost)
    else:
        cost = weight * 4.75 + 20
        print(cost)
    return cost

# ground_shipping()


# Ground Shipping Premium:
def ground_shipping_premium():
    weight = float(input("How much does your package weight?"))
    cost = weight + 125
    print("Total cost: ")
    print(cost)
    return cost

# ground_shipping_premium()


# Drone Shipping:
def drone_shipping():
    weight = float(input("How much does your package weight?"))
    if weight <= 2:
        cost = weight * 4.50
        print(cost)
    elif 2 < weight <= 6:
        cost = weight * 9
        print(cost)
    elif 6 < weight <= 10:
        cost = weight * 12
        print(cost)
    else:
        cost = weight * 14.25
        print(cost)

    return cost

# drone_shipping()


def choose_shipping():
    my_shipping = int(input("Please choose one of the following shipments by pressing 1, 2 or 3: \n"
                            "1- Ground shipping \n"
                            "2- Ground shipping premium \n"
                            "3- Drone shipping"))
    if my_shipping == 1:
        ground_shipping()
    elif my_shipping == 2:
        ground_shipping_premium()
    else:
        drone_shipping()

    return my_shipping


choose_shipping()

exit()
