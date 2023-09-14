"""
Weight Converter
How it works:
User inputs the weight to be converted to K for kg or P for pound.
1 kilogram (kg) is equal to 2.20462262185 pounds (lbs). 1 kg = 2.20462262185 lb.
"""
import sys

# Constants
K = 2.204
P = 0.453


def weight_converter(weight, wtype):
    if wtype == 'K' or wtype == 'k':
        return K * weight
    elif wtype == 'P' or wtype == 'p':
        return P * weight
    else:
        return "Invalid type selected"


def main():
    weight = int(input("Please type your weight: "))
    wtype = input("Please, choose type to convert to: K for kg and P for pounds: ")
    print(weight_converter(weight, wtype))


if __name__ == '__main__':
    main()

sys.exit(0)
