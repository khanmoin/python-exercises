"""
  Defining functions in python
"""


"""
  function to sum two numbers
  takes two integers as arguments
"""
def sum(num1: int, num2: int):
    return num1 + num2


def main():
    try:
        num1 = int(input("Enter Number: "))
        num2 = int(input("Enter Another Number: "))
    except ValueError:
        print("Please Enter Valid Number")
        exit(1)

    result = sum(num1, num2)
    print(f'{num1} + {num2} = {result}')


if __name__ == '__main__':
    main()
