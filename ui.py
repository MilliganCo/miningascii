# ui.py
import pygame
from settings import FONT_NAME, FONT_SIZE


class UI:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)

    def draw(self):
        # Пример: вывод информации об игроке в левом верхнем углу экрана
        text_surface = self.font.render("Health: 100", True, (255, 255, 255))
        self.screen.blit(text_surface, (10, 10))
