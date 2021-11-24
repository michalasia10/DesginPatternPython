from abc import ABC
from enum import Enum, auto


class HotDrink(ABC):
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print('This tea')


class Coffe(HotDrink):
    def consume(self):
        print('This coffe')


class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Put in tea bag, boil water, pour {amount}ml')
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Grind some beans, boil water, pour {amount}ml')
        return Coffe()


def make_drink(type) -> TeaFactory or CoffeeFactory:
    if type == 'tea':
        return TeaFactory().prepare(250)
    elif type == 'coffe':
        return CoffeeFactory().prepare(50)
    else:
        return None

class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFEE = auto()
        TEA = auto()

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name[0] +d.name[1:].lower()
                factory_name = name +'Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name,factory_instance))

    def make_drink(self):
        print('Avaiable drinks:')
        for f in self.factories:
            print(f[0])

        s = input(f'Please pick drink (0 - {len(self.factories) - 1})')
        idx = int(s)
        s = input(f'Specify amount')
        amount = int(s)
        return self.factories[idx][1].prepare(amount)

if __name__ == '__main__':
    hdm = HotDrinkMachine()
    hdm.make_drink()
