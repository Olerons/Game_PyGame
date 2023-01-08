import pygame
from debug import debug
from settings import *
from tile import Tile
from player import Player
from helper_def import import_csv_layout

class Level:
    def __init__(self):
        self.screen = pygame.display.get_surface()

        self.visible_sprites = CameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'X':
                    Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'P':
                    self.player = Player((x,y), [self.visible_sprites], self.obstacle_sprites )

    def draw(self):
        # теперь мы рисуем спрайты с помощью нашего отдельного метода
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        debug(self.player.direction)


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.half_width = self.screen.get_size()[0] // 2
        self.half_height = self.screen.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # задний фон задаем картинкой
        self.bg_surf = pygame.image.load('../data/map/world_map.png')
        self.bg_rect = self.bg_surf.get_rect(topleft=(0,0))

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # двигаем фон так же, как и все остальные спрайты
        bg_offset = self.bg_rect.topleft - self.offset
        self.screen.blit(self.bg_surf, bg_offset)

        for sprite in sorted(self.sprites(), key=lambda sprt: sprt.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.screen.blit(sprite.image, offset_pos)

