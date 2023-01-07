import pygame
from settings import *
from helper_def import load_img

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = load_img('../data/test/wall.png')
        self.rect = self.image.get_rect(topleft = pos)