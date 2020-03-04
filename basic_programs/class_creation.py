"""
  Creting classes in Python
"""


class Person:
    name = ""
    age = ""
    address = ""

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


    def get_details(self):
        return f'Name: {self.name}\nAge: {self.age}\nAddress: {self.address}'


def main():
    p1 = Person("Rashid", 25, "USA")
    p2 = Person("Basit", 23, "UK")
    p3 = Person("Zubair", 24, "UAE")

    print(p1.get_details())
    print(p2.get_details())
    print(p3.get_details())


if __name__ == '__main__':
    main()
