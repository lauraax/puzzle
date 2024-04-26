import pygame 
from pygame.sprite import Sprite
from pygame.locals import *

class Cuadritos(Sprite):
    def __init__(self, tablero, cont):
        Sprite.__init__(self)
        self.tablero = tablero
        self.cont = cont
        self.imagen = pygame.image.load("imagenes/cuadrito.png")
        self.rect = self.imagen.get_rect()
        self.vel = 5
        self.rect.move_ip(cont[0]//4, cont[1]//5)

    def actualizar_posicion(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.vel
        if keys[pygame.K_UP]:
            self.rect.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.rect.y += self.vel

        # Restringir el rectángulo dentro de los límites del tablero
        self.rect.clamp_ip(self.tablero.rect)