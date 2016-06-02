import pygame
from pygame.locals import *


class Pantalla():
    def __init__(self,screen,fondo):
        self.fondo = fondo
        self.screen = screen
    def actualizar(self,items):
        self.screen.blit(self.fondo, (0, 0))
        for i in items:
            self.screen.blit(i.imagen,i.rectangulo)

class Pantalla1(Pantalla):
    def __init__(self,screen):
        self.fondo = pygame.image.load("./imagenes/fondo_pantalla1.png")
        Pantalla.__init__(self,screen,self.fondo)
class Pantalla2(Pantalla):
    def __init__(self,screen):
        self.fondo = pygame.image.load("./imagenes/fondo_pantalla2.png")
        Pantalla.__init__(self,screen,self.fondo)


