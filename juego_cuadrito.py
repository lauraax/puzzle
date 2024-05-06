import pygame, sys, random
from pygame.sprite import Sprite
from pygame.locals import *
from cuadritos import *
from settings import *

#encapsulamos todos los procesos del juego en la clase Game
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Puzzle Deslizante")
        self.cuadritos = []
        
        # hacemos la lista de cuadritos

        coordenadas = [(x, y) for y in range(FILAS) for x in range(COL) if (x, y) != (COL - 1, FILAS - 1)]#creamos una lista de coordenadas para los cuadritos excluyendo la pos del vacio
        random.shuffle(coordenadas)  #las randomizamos
        for i in range(FILAS * COL - 1):  # hacemos el bucle sin que agregue un cuadro adicional
            valor = i + 1 #numero del cuadrito
            x, y = coordenadas[i]
            cuadrito = Cuadritos(valor, x, y)
            self.cuadritos.append(cuadrito)  #agregar el cuadrito a la lista de cuadritos
        
        random.shuffle(self.cuadritos) #se supone q esto desordena los cuadritos pero no :c 
        self.cuadro_vacio = CuadroVacio(COL - 1, FILAS - 1) 
 
        

    #funcion para hacer el blit de cada cuadrito en la lista cuadritos
    def dibujar_cuadritos(self):
        self.screen.fill(BLACK)
        for cuadrito in self.cuadritos:
            self.screen.blit(cuadrito.image, cuadrito.rect)
        # for cuadrito in self.cuadritos:
        #     print(cuadrito)
        pygame.display.flip()
        

    #funcion para que el cuadro vacio se mueva y este mueva los otros cuadritos
    def mover_cuadrito(self, dx, dy):
        x, y = self.cuadro_vacio.x + dx, self.cuadro_vacio.y + dy #establecemos las cordenadas

        for cuadrito in self.cuadritos:
            if cuadrito.rect.topleft == (x * TILE_SIZE, y * TILE_SIZE):
                cuadrito.rect.topleft = self.cuadro_vacio.x * TILE_SIZE, self.cuadro_vacio.y * TILE_SIZE
                self.cuadro_vacio.x, self.cuadro_vacio.y = x, y
                return



    def start(self):
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN: #movimiento del cuadro vacio
                    if event.key == pygame.K_LEFT:
                        self.mover_cuadrito(1, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.mover_cuadrito(-1, 0)
                    elif event.key == pygame.K_UP:
                        self.mover_cuadrito(0, 1)
                    elif event.key == pygame.K_DOWN:
                        self.mover_cuadrito(0, -1)
                    
            
            self.dibujar_cuadritos()
            


        pygame.quit()
        sys.exit()

game = Game()
game.start()


