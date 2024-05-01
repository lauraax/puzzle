import pygame
from pygame.sprite import Sprite
from pygame.locals import *
from settings import *

# Clase para la ficha vacía
class CuadroVacio:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Clase para las fichas numeradas
class Cuadritos(pygame.sprite.Sprite):
    def __init__(self, number, x, y):
        super().__init__()
        self.number = number
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(WHITE)
        pygame.draw.rect(self.image, COLORS[number % len(COLORS)], (3, 3, TILE_SIZE - 6, TILE_SIZE - 6))
        pygame.draw.rect(self.image, BLACK, (0, 0, TILE_SIZE, TILE_SIZE), 3)
        font = pygame.font.Font(None, 36)
        text = font.render(str(number), True, WHITE)
        text_rect = text.get_rect(center=(TILE_SIZE // 2, TILE_SIZE // 2))
        self.image.blit(text, text_rect)
        self.rect = self.image.get_rect(topleft=(x * TILE_SIZE, y * TILE_SIZE))
        self.x = x
        self.y = y