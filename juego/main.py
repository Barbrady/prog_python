import pygame,sys
from pygame.locals import *

ALTO = 1024
ANCHO = 1280

class Personaje(pygame.sprite.Sprite):
    def __init__(self,fichero):
        self.imagen = cargar_imagen(fichero,True)
        self.imagen_der = self.imagen
        self.imagen_izq =  pygame.transform.flip(self.imagen,True,False)
        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.centerx = 100
        self.rectangulo.centery = 100
        self.velocidad = [0.5, 0.5]

    def mover(self, tiempo, teclas):
        if self.rectangulo.top >= 0:
            if teclas[K_UP]:
                self.rectangulo.centery -= self.velocidad[1] * tiempo
        if self.rectangulo.bottom <= ALTO:
            if teclas[K_DOWN]:
                self.rectangulo.centery += self.velocidad[1] * tiempo
        if self.rectangulo.left >= 0:
            if teclas[K_LEFT]:
                self.rectangulo.centerx -= self.velocidad[0] * tiempo
                self.imagen = self.imagen_izq
        if self.rectangulo.right <= ANCHO:
            if teclas[K_RIGHT]:
                self.rectangulo.centerx += self.velocidad[0] * tiempo
                self.imgen = self.imagen_der




def cargar_imagen(fichero, transparente=False):
    imagen = pygame.image.load(fichero)
    if transparente == True:
        color = imagen.get_at((0,0))
        imagen.set_colorkey(color, RLEACCEL)
    return imagen
def main():
    pantalla = pygame.display.set_mode((ANCHO,ALTO))
    fondo = cargar_imagen("./imagenes/fondo.png")
    queco = Personaje("./imagenes/queco.png")
    clock = pygame.time.Clock()
    while True:
        teclas = pygame.key.get_pressed()
        tiempo = clock.tick(30)
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
        queco.mover(tiempo,teclas)
        pantalla.blit(fondo,(0,0))
        pantalla.blit(queco.imagen,queco.rectangulo)
        pygame.display.flip()
    return 0

if __name__ == '__main__' :
    print ('Este es el modulo main.')
    pygame.init()
    main()
