import pygame
from items import *
from pygame.locals import *


class Pantalla():
    def __init__(self,screen,fondo):
        self.fondo = fondo
        self.screen = screen
        self.items = []
    def actualizar(self,item):
        self.items = self.items+item
        self.screen.blit(self.fondo, (0, 0))
        for i in self.items:
            self.screen.blit(i.imagen, i.rect)

class Pantalla1(Pantalla):
    def __init__(self,screen):
        self.fondo = pygame.image.load("./imagenes/fondo_pantalla1.png")
        Pantalla.__init__(self,screen,self.fondo)
        bomba1 = Bomba((150,100))
        bomba2 = Bomba((400,600))
        self.items = [bomba1,bomba2]
class Pantalla2(Pantalla):
    def __init__(self,screen):
        self.fondo = pygame.image.load("./imagenes/fondo_pantalla2.png")
        Pantalla.__init__(self,screen,self.fondo)


