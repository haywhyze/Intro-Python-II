# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:

    def __init__(self, name, current_room, items=[]):
        self.name = name
        self.items = items
        self.current_room = current_room

    def getCurrentRoom(self):
        return self.current_room

    def getName(self):
        return self.name

    def setCurrentRoom(self, room):
        self.current_room = room
    
    def printInventory(self):
        inventory_str = ""
        if len(self.items) == 0:
            return print("No items in your inventory")
        for item in self.items:
            inventory_str += ("\n"+ item.name)
        return print(f"\nItems in your inventory: {inventory_str}")