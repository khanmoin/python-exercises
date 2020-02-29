"""
  Lambda Functions in Python
"""


def add_simple(x, y):
    return x + y

add_lambda = lambda x,y : x + y


def main():
    # Adding using simple function
    print(add_simple(10, 20))

    # Adding using lambda function
    print(add_lambda(10, 20))


if __name__ == '__main__':
    main()
