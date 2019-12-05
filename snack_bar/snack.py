import uuid


class Snack:
    def __init__(self, name, quantity, cost, vending_machine_id):
        self.id = uuid.uuid4()
        self.name = name
        self.quantity = quantity
        self.cost = cost
        self.vending_machine_id = vending_machine_id

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, new_name):
        self.name = new_name

    def getQuantity(self):
        return self.quantity

    def addQuantity(self, quantity):
        self.quantity += quantity

    def buySnack(self, quantity):
        self.quantity -= quantity

    def getTotalCost(self, quantity):
        return quantity * self.cost
