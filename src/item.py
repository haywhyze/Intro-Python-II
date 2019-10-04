class Item:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f"You have picked up {self.name.capitalize()}")
    
    def on_drop(self):
        print(f"You just dropped {self.name.capitalize()}")

    def __str__(self):
        return self.name