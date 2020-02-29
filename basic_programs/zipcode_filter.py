"""
  Filtering zipcodes from text
"""


def main():
    txt = input("Enter text with zip code: ")
    filtered = list(filter(lambda x: len(x) == 6 and x.isnumeric(), txt.split()))
    print(filtered)


if __name__ == '__main__':
    main()
