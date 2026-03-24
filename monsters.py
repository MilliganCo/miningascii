# monsters.py
from settings import FONT_SIZE

class Monster:
    def __init__(self, x, y, char, color, hp):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.hp = hp

    def move_towards_player(self, player):
        # Простейшая логика: шаг в сторону игрока по оси X и Y
        if self.x < player.x:
            self.x += 1
        elif self.x > player.x:
            self.x -= 1
        if self.y < player.y:
            self.y += 1
        elif self.y > player.y:
            self.y -= 1

    def update(self, player):
        self.move_towards_player(player)

    def get_screen_position(self):
        return (self.x * FONT_SIZE, self.y * FONT_SIZE)

    def get_ascii(self):
        return self.char

    def get_color(self):
        return self.color

class Boss(Monster):
    def __init__(self, x, y):
        # Босс с повышенными характеристиками
        super().__init__(x, y, 'B', (255, 0, 0), hp=50)
