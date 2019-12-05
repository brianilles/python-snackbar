import uuid


class VendingMachine:
    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, new_name):
        self.name = new_name


example_vending_machine = VendingMachine("Vending Machine")
print(example_vending_machine.getId())
print(example_vending_machine.getName())

example_vending_machine.setName("Updated name")
print(example_vending_machine.getName())
