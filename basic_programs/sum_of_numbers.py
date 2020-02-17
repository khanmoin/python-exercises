"""
  Calculating the sum of numbers
"""


"""
  calculates the sum of n numbers
  takes input integer num and calculates sum from 1 to num
"""
def sum_of_nums(num):
    sum = 0
    for i in range(num):
        sum += i + 1
    return sum


def main():
    try:
        num = int(input("Enter Number: "))
    except ValueError:
        print("Invalid Input")

    result = sum_of_nums(num)
    print(result)


if __name__ == '__main__':
    main()

