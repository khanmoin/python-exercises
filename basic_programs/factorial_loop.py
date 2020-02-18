"""
  Calculating factorial of a number using loops
"""


def fact(num):
    result = 1
    for i in range(num):
        result *= i+1
    return result


def main():
    try:
        num = int(input("Enter number: "))
    except ValueError:
        print("Invalid Input")

    result = fact(num)
    print(f'{num}! = {result}')


if __name__ == '__main__':
    main()
