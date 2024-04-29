import pygame, sys
from pygame.sprite import Sprite
from pygame.locals import *
from tablero import *
from cuadritos import *

#definimos colores
BLACK = (0,0,0)

# definir el tamaño de la pantalla
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
reloj = pygame.time.Clock()

#definimos variables a utilizar
GAME_SIZE = 3

#asignamos la clase Tablero al objeto tablero
tablero = Tablero(size)
cuadrito = Cuadritos(tablero, size)


def main ():
    pygame.init
    pygame.mixer.init()
    
    #fondo
    background_image = pygame.image.load("imagenes/space.jpg")
    background_rect = background_image.get_rect()
    pygame.display.set_caption("Puzzle")
    surface = pygame.Surface((tablero.rect.width, tablero.rect.height))

    #funcion dibujar cuadricula
    def dibujar_cuadricula(surface, cuadrito):
        for fila in range(-1, tablero.rect.height, cuadrito):
            pygame.draw.line(surface, BLACK, (0, fila), (tablero.rect.width, fila), 2)
        for columna in range(-1, tablero.rect.width, cuadrito):
            pygame.draw.line(surface, BLACK, (columna, 0), (columna, tablero.rect.height), 2)


    game = True
    
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.blit(background_image, background_rect)
        screen.blit(tablero.image, tablero.rect)
        screen.blit(cuadrito.imagen, cuadrito.rect)
        keys = pygame.key.get_pressed()
        cuadrito.actualizar_posicion(keys)

        image_copy = tablero.image.copy()
        dibujar_cuadricula(image_copy, cuadrito.tamaño)
        screen.blit(image_copy, tablero.rect)
        

        pygame.display.update()
        reloj.tick(60)
if __name__ == '__main__':
    main()