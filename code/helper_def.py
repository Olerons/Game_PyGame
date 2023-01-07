import pygame
from settings import *
pygame.init()

def load_img(file, colorkey=None):
    img = pygame.image.load(file)
    if colorkey:
        img = img.convert()
        if colorkey == -1:
            colorkey = img.get_at((0, 0))
        img.set_colorkey(colorkey)
    else:
        img = img.convert_alpha()
    img = pygame.transform.scale(img, (TILESIZE, TILESIZE))
    return img