import pygame,sys, types
from pantallas import *
from pygame.locals import *
from items import *

ALTO = 1024
ANCHO = 1280

def cargar_imagen(fichero, transparente=False):
    imagen = pygame.image.load(fichero)
    if transparente == True:
        color = imagen.get_at((0,0))
        imagen.set_colorkey(color, RLEACCEL)
    return imagen
def main():
    screen = pygame.display.set_mode((ANCHO,ALTO))
    pygame.display.set_caption("Videojuego")
    #fondo = cargar_imagen("./imagenes/fondo_pantalla2.png")
    queco = Protagonista("./imagenes/queco.png",(50,50))
    #bomba = Personaje("./imagenes/bomba.png",(300,300))
    #bomba.situar((300,300))
    items = [queco]
    pantalla = Pantalla1(screen)
    items = pantalla.get_items()
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
        #pantalla.actualizar(items)
        screen.blit(pantalla.fondo,(0,0))
        screen.blit(queco.imagen,queco.rect)
        for i in items:
            screen.blit(i.imagen,i.rect)
            if isinstance(i, Bomba) and queco.rect.colliderect(i.rect): sys.exit(0)
        #pantalla.blit(fondo,(0,0))
        #pantalla.blit(bomba.imagen,bomba.rectangulo)
        #pantalla.blit(queco.imagen,queco.rectangulo)
        print(clock.get_fps())
        pygame.display.flip()
    return 0

if __name__ == '__main__' :
    print ('Este es el modulo main.')
    pygame.init()
    main()
