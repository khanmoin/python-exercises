"""
  Applying logistic function to a given list of numbers
"""


import math


def main():
    lst = input("Enter list of numbers seperated by spaces: ")
    try:
        lst = [int(x) for x in lst.split()]
    except ValueError:
        print("Invalid Input")

    result = list(map(lambda x : 1 / (1 + math.exp(-x)), lst))
    print(result)


if __name__ == '__main__':
    main()
