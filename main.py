from abc import ABC, abstractmethod
import json


class Component(ABC):

    @abstractmethod
    def description(self):
        pass

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def price(self):
        pass


class Leaf(Component):

    def name(self):
        return self.__name

    def description(self):
        print(self.__description)

    def price(self):
        return self.__price

    def __init__(self, name, price, description):
        self.__name = name
        self.__price = price
        self.__description = description


class Composite(Component):

    def __init__(self, name, components):
        self.__name = name
        self.__components = components

    def description(self):
        print(f'{self.__name:_^50}')
        for component in self.__components:
            component.description()
        print(f'{"":_^50}')

    def name(self):
        for component in self.__components:
            print(component.name())

    def price(self):
        total = 0
        for component in self.__components:
            total += component.price()
        return total

    def add(self, component):
        self.__components.append(component)


if __name__ == '__main__':

    f = open('data.json')
    data = json.load(f)
    # Closing file
    f.close()

    computer = Composite("Computer", [])
    motherboard = Composite("Motherboard", [])
    peripherals = Composite("Peripherals", [])

    option = 1

    while option != 0:
        print("1. Show computer motherboard")
        print("2. Show computer peripherals")
        print("3. Add new component")
        option = int(input("Enter a number: "))

        if option == 1:
            print("Total price motherboard:", motherboard.price(), 'eur')
        elif option == 2:
            print("Total price peripherals:", peripherals.price(), 'eur')
        elif option == 3:
            print("Which component you would like to add? ")
            print("1. Hard disk?")
            print("2. Peripherals?")
            read = int(input("Enter a number: "))
            if read == 1:
                for disk in data['hard_disks']:
                    print(disk['name'])
                temp = int(input("Enter a Number: "))
                motherboard.add(Leaf(data['hard_disks'][temp-1]['name'],
                                     data['hard_disks'][temp-1]['price'],
                                     data['hard_disks'][temp-1]['description']))
            else:
                for disk in data['peripherals']:
                    print(disk['name'])

        elif option == 0:
            quit()
