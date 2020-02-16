"""
  perfroming a linear search on a list of numbers
"""


def linear_search(lst, key):
    for element in lst:
        if element == key:
            return element
    return -1


def main():
    lst = input("Enter Elements of the list: ")     # taking input from the user
    try:
        lst = [int(x) for x in lst.split()]             # using list comprehension to clean and convert data
    except ValueError as err:
        print(f"Invalid input enter numbers only.\n{err}")
        exit(1)
    key = int(input("Enter element you want to look for: "))
    result = linear_search(lst, key)
    if result == -1:
        print(f"{key} not found in the list")
    else:
        print(f"{key} is in the list")


if __name__ == "__main__":
    main()
