import pygame
from pygame.locals import *
from main import ALTO,ANCHO

def cargar_imagen(fichero_imagen, transparente=False):
    imagen = pygame.image.load(fichero_imagen)
    imagen.convert()
    if transparente == True:
        color = imagen.get_at((0, 0))
        imagen.set_colorkey(color, RLEACCEL)
    return imagen

class Item(pygame.sprite.Sprite):
    def __init__(self,fichero_imagen,posicion):
        self.imagen = cargar_imagen(fichero_imagen,True)
        self.rect = self.imagen.get_rect()
        self.rect.centerx = posicion[0]
        self.rect.centery = posicion[1]
    def situar(self,situacion):
        self.rect.centerx = situacion[0]
        self.rect.centery = situacion[1]
class Bomba(Item):
    def __init__(self,posicion):
        Item.__init__(self,"./imagenes/bomba.png",posicion)
class Personaje(Item):
    def __init__(self,fichero_imagen,posicion):
        Item.__init__(self,fichero_imagen,posicion)
        self.velocidad = [0.3, 0.3]
        self.situacion = (self.rect.centerx, self.rect.centery)
        self.derecha = True
        self.izquierda = False
    def rotar_imagen(self):
        self.imagen = pygame.transform.flip(self.imagen, True, False)

class Protagonista(Personaje):
    def __init__(self,fichero_imagen,posicion):
        Personaje.__init__(self,fichero_imagen,posicion)
    def mover(self, tiempo, teclas):
        if self.rect.top >= 0:
            if teclas[K_UP]:
                self.rect.centery -= self.velocidad[1] * tiempo
        if self.rect.bottom <= ALTO:
            if teclas[K_DOWN]:
                self.rect.centery += self.velocidad[1] * tiempo
        if self.rect.left >= 0:
            if teclas[K_LEFT]:
                if self.derecha:
                    self.rotar_imagen()
                    self.derecha = False
                    self.izquierda = True
                self.rect.centerx -= self.velocidad[0] * tiempo
        if self.rect.right <= ANCHO:
            if teclas[K_RIGHT]:
                if self.izquierda:
                    self.rotar_imagen()
                    self.derecha = True
                    self.izquierda = False
                self.rect.centerx += self.velocidad[0] * tiempo

