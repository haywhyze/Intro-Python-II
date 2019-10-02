# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:

    def __init__(self, name, current_room):
        self.current_room = current_room

    def getCurrentRoom(self):
        return self.current_room

    def getName(self):
        return self.name

    def setCurrentRoom(self, room):
        self.current_room = room