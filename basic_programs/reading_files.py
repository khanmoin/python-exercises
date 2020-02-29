"""
  Reading text files with Python
"""


def main():
    # reading whole file, with autocloses the file after the end of block
    with open("hello.txt") as f:
        print(f.read())

    # reading 10 characters
    with open("hello.txt") as f:
        print(f.read(10))

    # reading one line
    with open("hello.txt") as f:
        print(f.readline())

        
if __name__ == '__main__':
    main()
