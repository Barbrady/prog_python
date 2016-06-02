import pygame,sys
from pantallas import *
from pygame.locals import *

ALTO = 1024
ANCHO = 1280

class Personaje(pygame.sprite.Sprite):
    def __init__(self,fichero,posicion):
        self.imagen = cargar_imagen(fichero,True)
        self.derecha = True
        self.izquierda = False
        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.centerx = posicion[0]
        self.rectangulo.centery = posicion[1]
        self.rect = self.rectangulo
        self.velocidad = [0.3, 0.3]
        self.situacion = (self.rectangulo.centerx,self.rectangulo.centery)

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
    screen = pygame.display.set_mode((ANCHO,ALTO))
    #fondo = cargar_imagen("./imagenes/fondo_pantalla2.png")
    queco = Personaje("./imagenes/queco.png",(50,50))
    bomba = Personaje("./imagenes/bomba.png",(300,300))
    #bomba.situar((300,300))
    items = (queco,bomba)
    pantalla = Pantalla1(screen)
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
        pantalla.actualizar(items)
        #pantalla.blit(fondo,(0,0))
        #pantalla.blit(bomba.imagen,bomba.rectangulo)
        #pantalla.blit(queco.imagen,queco.rectangulo)
        if pygame.sprite.collide_rect(queco,bomba): pantalla = Pantalla2(screen)
        pygame.display.flip()
    return 0

if __name__ == '__main__' :
    print ('Este es el modulo main.')
    pygame.init()
    main()
