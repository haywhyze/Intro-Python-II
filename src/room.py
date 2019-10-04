# Implement a class to hold room information. This should have name and
# description attributes.
class Room:

    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def getRoomName(self):
        return self.name

    def getRoomDescription(self):
        return self.description
    
    def items_str(self):
        item_str = ""
        if len(self.items) == 0:
            item_str = "No items in this room"
        for item in self.items:
            item_str += ("\n "+ item.name)
        return item_str
    def __str__(self):
        return f"\nCurrent Room: {self.name} - {self.description}\n\nItems: {self.items_str()}"