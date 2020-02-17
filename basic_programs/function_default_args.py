"""
  Defining function with default arguments
"""


"""
  function to calculate exponantial power
  takes two integers as input, base and exponant, exponant defaults to 2
"""
def raise2power(num: int, power: int=2) -> int:
    sum = 1
    for i in range(power):
        sum *= num
    return sum

def main():
    try:
        num = int(input("Enter Number: "))
        power = int(input("Enter power: "))
    except ValueError:
        print("Invalid input")
        exit(1)

    result = raise2power(num, power)
    default_result = raise2power(num)
    print(f'{num}^{power} = {result}')
    print(f'Default Result: {num}^2 = {default_result}')

if __name__ == '__main__':
    main()
