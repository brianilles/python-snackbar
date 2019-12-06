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
