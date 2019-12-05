from vending_machine import VendingMachine
from snack import Snack
from customer import Customer


def snackBar():
    # create Customers
    c1 = Customer("Jane", 90.00)
    c2 = Customer("Bob", 60.00)

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

    print(f"{c1.getName()} now has: {c1.getCash()}")

    print(c1.getCash())  # 57.0
    print(s4.getQuantity())  # 197


if __name__ == '__main__':
    snackBar()
