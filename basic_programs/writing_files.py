"""
  Writing some quotes to a file
"""


import random


QUOTES_FILE = "quotes.txt"

def add_quote(quote):
    with open(QUOTES_FILE, "a") as f:
        f.write(quote + '\n')


def read_quote():
    try:
        with open(QUOTES_FILE) as f:
            quotes = f.readlines()
            if not quotes:
                print("No quote Added Yet")
            else:
                index = random.randrange(0, len(quotes))
                print(quotes[index])
    except FileNotFoundError:
        print("Quotes file has not been initialized yet")


def main():
    resp = input("a - add quote\nv - view a random quote\nq - quit\n$: ")
    while resp != 'q':
        if resp == 'a':
            quote = input("Enter quote to add: ")
            add_quote(quote)
        elif resp == 'v':
            read_quote()
        resp = input("\na - add quote\nv - view a random quote\nq - quit\n$: ")


if __name__ == '__main__':
    main()
