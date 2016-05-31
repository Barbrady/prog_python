import pygame,sys
from pygame.locals import *

ALTO = 640
ANCHO = 800

class Personaje(pygame.sprite.Sprite):
    def __init__(self,fichero):
        self.imagen = cargar_imagen(fichero,True)
        self.derecha = True
        self.izquierda = False
        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.centerx = 100
        self.rectangulo.centery = 100
        self.rect = self.rectangulo
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
                if self.derecha:
                    self.rotar_imagen()
                    self.derecha = False
                    self.izquierda = True
                self.rectangulo.centerx -= self.velocidad[0] * tiempo
        if self.rectangulo.right <= ANCHO:
            if teclas[K_RIGHT]:
                if self.izquierda:
                    self.rotar_imagen()
                    self.derecha = True
                    self.izquierda = False
                self.rectangulo.centerx += self.velocidad[0] * tiempo
    def rotar_imagen(self):
        self.imagen = pygame.transform.flip(self.imagen,True,False)
    def situar(self,posicion):
        self.rectangulo.centerx = posicion[0]
        self.rectangulo.centery = posicion[1]




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
    bomba = Personaje("./imagenes/bomba.png")
    bomba.situar((300,300))
    clock = pygame.time.Clock()
    pygame.mixer.music.load("./sound/bso.ogg")
    pygame.mixer.music.play()
    while True:
        teclas = pygame.key.get_pressed()
        tiempo = clock.tick(30)
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
        queco.mover(tiempo,teclas)
        pantalla.blit(fondo,(0,0))
        pantalla.blit(bomba.imagen,bomba.rectangulo)
        pantalla.blit(queco.imagen,queco.rectangulo)
        if pygame.sprite.collide_rect(queco,bomba): sys.exit(0)
        pygame.display.flip()
    return 0

if __name__ == '__main__' :
    print ('Este es el modulo main.')
    pygame.init()
    main()
