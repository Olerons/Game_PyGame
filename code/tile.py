import pygame
from settings import *
from helper_def import load_img

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, surf=pygame.Surface((TILESIZE,TILESIZE))):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)

        # у спрайта тайла тоже должен быть hitbox.
        # это очень поможет в дальнейшем
        self.hitbox = self.rect.inflate(0, -10)