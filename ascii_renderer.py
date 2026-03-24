import pygame
from settings import FONT_NAME, FONT_SIZE


class ASCIIRenderer:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)

    def render_world(self, world):
        # Пример: отрисовка карты мира символами
        for tile in world.get_visible_tiles():
            char = tile.get_ascii()  # должен возвращать символ
            color = tile.get_color()
            pos = tile.get_screen_position()
            text_surface = self.font.render(char, True, color)
            self.screen.blit(text_surface, pos)

    def render_player(self, player):
        # Отрисовка игрока в его текущей позиции
        pos = player.get_screen_position()
        text_surface = self.font.render('@', True, (255, 255, 255))
        self.screen.blit(text_surface, pos)
