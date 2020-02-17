"""
  Calculating the fibonacci number using loop
"""


def fibonacci(num):
    prev = 0
    curr = 1
    for i in range(num-1):
        new_num = prev + curr
        prev = curr
        curr = new_num
    return new_num


def main():
    try:
        num = int(input("Enter Number: "))
    except ValueError:
        print("Invalid Input")
        exit(1)

    result = fibonacci(num)
    print(result)

if __name__ == '__main__':
    main()
