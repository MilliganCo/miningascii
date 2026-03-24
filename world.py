# world.py
import random
from settings import FONT_SIZE

class Tile:
    def __init__(self, x, y, type_char, color):
        self.x = x
        self.y = y
        self.type_char = type_char
        self.color = color

    def get_ascii(self):
        return self.type_char

    def get_color(self):
        return self.color

    def get_screen_position(self):
        return (self.x * FONT_SIZE, self.y * FONT_SIZE)

class World:
    def __init__(self, width=50, height=30):
        self.width = width
        self.height = height
        self.tiles = []
        self.generate_world()

    def generate_world(self):
        # Генерация простого уровня: верхние ряды – поверхность, остальные – подземелье
        for y in range(self.height):
            row = []
            for x in range(self.width):
                if y < 5:
                    # Поверхность: трава
                    tile = Tile(x, y, '.', (0, 255, 0))
                else:
                    # Подземелье: камень
                    tile = Tile(x, y, '#', (100, 100, 100))
                row.append(tile)
            self.tiles.append(row)

    def get_visible_tiles(self):
        # Возвращаем все тайлы (при желании можно добавить алгоритм видимости)
        visible = []
        for row in self.tiles:
            visible.extend(row)
        return visible

    def update(self):
        # Здесь можно добавить логику обновления мира (например, смену состояния блоков)
        pass
