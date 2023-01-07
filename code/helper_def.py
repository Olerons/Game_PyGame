import pygame
from settings import *
from csv import reader


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
    # устанавливаю размеры спрайта под размеры плитки (tilesize)
    img = pygame.transform.scale(img, (TILESIZE, TILESIZE))
    return img

def import_csv_layout(path):
    map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter=',')
        for row in layout:
            map.append(list(row))
    return map