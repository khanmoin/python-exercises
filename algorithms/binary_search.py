"""
  perfroming a binary search on a list of numbers
"""


def binary_search(lst, lo, hi, key):
    while lo <= hi:
        mid = (lo+hi)//2
        if lst[mid] == key:
            return lst[mid]
        if lst[mid] > key:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

def main():
    lst = input("Enter Elements of the list: ")     # taking input from the user
    try:
        lst = [int(x) for x in lst.split()]             # using list comprehension to clean and convert data
    except ValueError as err:
        print(f"Invalid input enter numbers only.\n{err}")
        exit(1)
    key = int(input("Enter element you want to look for: "))
    result = binary_search(lst, 0, len(lst) - 1,key)
    if result == -1:
        print(f"{key} not found in the list")
    else:
        print(f"{key} is in the list")


if __name__ == "__main__":
    main()
