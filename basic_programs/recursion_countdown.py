"""
  Creating a Timer Countdown using recursion
"""


import time


def countdown(num):
    if num == 0:
        print("Done")
    else:
        print(num)
        time.sleep(1)
        countdown(num-1)


def main():
    try:
        num = int(input("Enter timer duration(in seconds): "))
    except ValueError:
        print("Invalid Input")

    countdown(num)


if __name__ == '__main__':
    main()
