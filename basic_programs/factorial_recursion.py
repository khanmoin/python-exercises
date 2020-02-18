"""
  Calculating factorial of using recursion
"""


def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num-1)


def main():
    try:
        num = int(input("Enter number: "))
    except ValueError:
        print("Invalid Input")

    result = fact(num)
    print(f'{num}! = {result}')


if __name__ == '__main__':
    main()
