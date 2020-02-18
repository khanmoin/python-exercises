"""
  Computing fibonacci number using recursion
"""


def fibonacci(num):
    if num == 0 or num == 1:
        return num
    else:
        return fibonacci(num-2) + fibonacci(num-1)


def main():
    try:
        num = int(input("Enter number: "))
    except ValueError:
        print("Invalid Input")

    result = fibonacci(num)
    print(result)


if __name__ == '__main__':
    main()
