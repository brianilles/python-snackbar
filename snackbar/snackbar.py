import sys

from vending_machine import VendingMachine
from snack import Snack
from customer import Customer


class Snackbar:
    """Main Snackbar Class"""

    def __init__(self, name):
        """Construct a new Snackbar"""
        self.name = name
        self.open = False
        self.actions = {
            "add new customer": self.addCustomer
        }

    def addCustomer(self, name, cash):
        c = Customer(name, int(cash))
        print(c)
        print(f"New customer {c.getName()} has ${c.getCash()}.00")

    def run(self):
        self.open = True

        while self.open:
            s = input("\nCommand> ").strip().split()  # .lower()
            action = " ".join(s[:3])
            args = s[3:]

            try:
                self.actions[action](*args)
            except:
                print(f"Unknown command '{s}'")
                sys.exit(1)


if __name__ == '__main__':
    exampleSnackbar = Snackbar("Python's Snackbar")
    exampleSnackbar.run()

    # create Vending Machines
    vm1 = VendingMachine("Food")
    vm2 = VendingMachine("Drink")

    # create Snacks
    s1 = Snack("Chips", 200, 1.00, vm1.getId())
    s2 = Snack("Chocolate Bar", 200, 1.00, vm1.getId())
    s3 = Snack("Pretzels", 200, 1.00, vm1.getId())

    s4 = Snack("Soda", 200, 1.00, vm2.getId())
    s5 = Snack("Water", 200, 1.00, vm2.getId())

    # 1. Customer 1 buys 3 of snack 4. Print Customer 1 Cash on hand. Print quantity of snack 4.
    print("\n--#1-----------")
    print(f"{c1.getName()}'s initial cash: {c1.getCash()}")

    print(c1.buyTotal(s4, 3))
    print(c1.buyTotal(s1, 100))

    print(c1.getCash())  # 57.0
    print(s4.getQuantity())  # 197
