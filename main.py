import pygame
from settings import *
from game import Game


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("ASCII Adventure")

    game = Game(screen)
    game.run()


if __name__ == '__main__':
    main()
