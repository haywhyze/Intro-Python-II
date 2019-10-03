import textwrap
from room import Room
from player import Player
from item import Item

wrapper = textwrap.TextWrapper(width=50)
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [
                         "book", "sword", "amulet", "knife"
                     ]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [
    "laptop", "phone", "guitar", "pen"
]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [
    ""
]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Declare all items

item = {
    'book': Item("Book", "A piece to take notes"),
    'sword': Item("Sword", "A weapon to fight enemies"),
    'amulet': Item("Amulet", "A good luck charm"),
    'knife': Item("Knife", "a tool with a cutting edge or blade attached to a handle"),
    'laptop': Item("Laptop", "a computer that is portable and suitable for use while travelling."),
    'phone': Item("Phone", "system for transmitting voices over a distance using wire or radio"),
    'guitar': Item("Guitar", "a stringed musical instrument")
}

# Link items to rooms

room['outside'].items = [
    item['book'],
    item['sword']
]

room['foyer'].items = [
    item['amulet'],
    item['knife'],
]

room['overlook'].items = [
    item['laptop'],
]

room['narrow'].items = [
    item['phone']
]

room['treasure'].items = [
    item['guitar']
]


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
vincent = Player("Vincent", room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

print('\n\tWelcome to The Adventure Game\n')
print('Please input: \n'
        + '\tn to move north\n'
        + '\ts to move south\n'
        + '\tw to move west\n'
        + '\te to move east')
print(vincent.getCurrentRoom())

while True:
    user_input = input('\nWhere would you like to go next: ')
    if user_input == "n":
        if hasattr(vincent.getCurrentRoom(), 'n_to'):
            vincent.setCurrentRoom(vincent.getCurrentRoom().n_to)
            print(vincent.getCurrentRoom())
        else:
            print(f"\nSorry there is nothing up north...\n")
    elif user_input == "w":
        if hasattr(vincent.getCurrentRoom(), 'w_to'):
            vincent.setCurrentRoom(vincent.getCurrentRoom().w_to)
            print(vincent.getCurrentRoom())
        else:
            print(f"\nSorry there is nothing to the west...\n")
    elif user_input == "s":
        if hasattr(vincent.getCurrentRoom(), 's_to'):
            vincent.setCurrentRoom(vincent.getCurrentRoom().s_to)
            print(vincent.getCurrentRoom())
        else:
            print(f"\nSorry there is nothing down south...\n")
    elif user_input == "e":
        if hasattr(vincent.getCurrentRoom(), 'e_to'):
            vincent.setCurrentRoom(vincent.getCurrentRoom().e_to)
            print(vincent.getCurrentRoom())
        else:
            print(f"\nSorry there is nothing to the east...\n")
    elif user_input == "q":
        print('\nThanks for playing... Come back for more fun\n')
        break
    else:
        print('\nWrong Input Please input: \n'
            + '\tn to move north\n'
            + '\ts to move south\n'
            + '\tw to move west\n'
            + '\te to move east\n')
