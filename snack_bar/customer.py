import uuid


class Customer:
    def __init__(self, name, cash):
        self.id = uuid.uuid4()
        self.name = name
        self.cash = cash

    def addCash(cash):
        self.cash += cash

    def buyTotal(self, snack, quantity):
        """
          Calculates the total cash used in purchase.
        """

        # we need to make sure the vending machine has the quanity available for that item
        # we need to make sure the customer has enough money to by the items

        snackQuantity = snack.getQuantity()
        if snackQuantity < quantity:
            need_plural = "s" if snackQuantity > 1 else ""
            return f"There's only {snackQuantity} {snack.getName()}{need_plural} available."
        else:
            total = snack.getTotalCost(quantity)

            if total > self.cash:
                return f"Insufficient funds. The total is {total}. And {self.name} only has {self.cash}."
            else:
                self.cash -= total
                snack.buySnack(quantity)
                need_plural = "s" if snackQuantity > 1 else ""
                return f"{quanity} {snack.getName()}{need_plural}  bought by {self.name}"

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getCash(self):
        return self.cash
