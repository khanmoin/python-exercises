"""
  Checking Whether a given number is prime or not
"""


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def main():
    try:
        num = int(input("Enter Number: "))
    except ValueError:
        print("Invalid Input")
        exit(1)

    if is_prime(num):
        print("Prime")
    else:
        print("Not Prime")


if __name__ == '__main__':
    main()
