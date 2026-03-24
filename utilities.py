# utilities.py
def load_sprite(path):
    import pygame
    return pygame.image.load(path)

def clamp(val, min_val, max_val):
    return max(min_val, min(val, max_val))
