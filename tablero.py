import pygame 
from pygame.sprite import Sprite
from pygame.locals import *

class Tablero (Sprite):
    def __init__(self, cont):
        Sprite.__init__(self)
        self.contenedor = cont
        self.image = pygame.image.load("imagenes/tablero.png")
        self.rect = self.image.get_rect()
        self.rect.move_ip(cont[0]//4, cont[1]//5)

