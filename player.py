# player.py
import pygame
from settings import FONT_SIZE

class Player:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.char = '@'
        self.color = (255, 255, 255)
        # Инициализация инвентаря: 10 ячеек, по умолчанию пустые
        self.inventory = [None] * 10
        self.selected_slot = 0
        self.skills = {"digging": 1, "crafting": 1, "combat": 1}
        self.experience = 0

    def update(self):
        # Обновление состояния игрока, например, повышение уровня
        self.check_level_up()

    def check_level_up(self):
        if self.experience >= 10:
            self.skills["digging"] += 1
            self.experience -= 10
            print("Уровень навыка копания повышен!")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def get_screen_position(self):
        return (self.x * FONT_SIZE, self.y * FONT_SIZE)

    def dig(self):
        # Здесь реализуется логика копания/сбора ресурсов:
        # Например, проверка текущей позиции, изменение мира и добавление ресурса в инвентарь.
        print("Действие копания выполнено!")
        # Пример: добавить ресурс в выбранную ячейку инвентаря, если она пуста
        if self.inventory[self.selected_slot] is None:
            self.inventory[self.selected_slot] = "resource"
            print(f"Ресурс добавлен в ячейку {self.selected_slot + 1}")
        else:
            print(f"Ячейка {self.selected_slot + 1} уже занята")
