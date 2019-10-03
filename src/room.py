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

    def __str__(self):
        item_str = ""
        for item in self.items:
            item_str += (" "+ item.name)
        return f"\nCurrent Room: {self.name} - {self.description}\n\nItems: {item_str}"