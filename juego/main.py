import pygame,sys
from pygame.locals import *

ALTO = 600
ANCHO = 600

def main():
    pantalla = pygame.display.set_mode((ANCHO,ALTO))
    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
    return 0

if __name__ == '__main__' :
    print ('Este es el modulo main.')
    pygame.init()
    main()
