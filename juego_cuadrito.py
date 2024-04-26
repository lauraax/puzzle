import pygame, sys
from pygame.sprite import Sprite
from pygame.locals import *
from tablero import *
from cuadritos import *
# definir el tamaño de la pantalla
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
reloj = pygame.time.Clock()

#asignamos la clase Tablero al objeto tablero
tablero = Tablero(size)
cuadrito = Cuadritos(tablero, size)
def main ():
    pygame.init
    pygame.mixer.init()
    

    background_image = pygame.image.load("imagenes/space.jpg")
    background_rect = background_image.get_rect()

    pygame.display.set_caption("Puzzle")
    
    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.blit(background_image, background_rect)
        screen.blit(tablero.image, tablero.rect)
        screen.blit(cuadrito.imagen, cuadrito.rect)
        keys = pygame.key.get_pressed()

        cuadrito.actualizar_posicion(keys)

        pygame.display.update()
        reloj.tick(60)
if __name__ == '__main__':
    main()