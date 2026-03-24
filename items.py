# items.py
class Item:
    def __init__(self, name, char, color):
        self.name = name
        self.char = char
        self.color = color

    def get_ascii(self):
        return self.char

class Resource(Item):
    def __init__(self, name, quantity=1):
        # Например, камень или руда
        super().__init__(name, '*', (200, 200, 0))
        self.quantity = quantity

class Key(Item):
    def __init__(self):
        super().__init__("Key", 'K', (0, 0, 255))

class Chest(Item):
    def __init__(self, locked=True):
        super().__init__("Chest", 'C', (139, 69, 19))
        self.locked = locked
        self.contents = []

    def unlock(self, key):
        if isinstance(key, Key):
            self.locked = False
            return True
        return False
