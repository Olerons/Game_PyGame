import pygame
from debug import debug
from settings import *
from tile import Tile
from player import Player
from helper_def import import_csv_layout, import_brushes

class Level:
    def __init__(self):
        self.screen = pygame.display.get_surface()

        self.visible_sprites = CameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        layouts = {
            'tower_bg': import_csv_layout('../data/map/world_map_tower.csv'),
            'tower_up': import_csv_layout('../data/map/world_map_tower2.csv'),
            'player': import_csv_layout('../data/map/world_map_player.csv'),
            'obstacle': import_csv_layout('../data/map/world_map_obstacle.csv')
        }

        brushes = {
            'world': import_brushes('../data/img/Overworld.png', (16,16))
        }

        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != -1:
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'tower_bg':
                            Tile((x,y), [self.visible_sprites], brushes['world'][int(col)])
                        if style == 'tower_up':
                            Tile((x, y), [self.visible_sprites], brushes['world'][int(col)])
                        if style == 'obstacle':
                            if col == '0':
                                Tile((x, y), [self.obstacle_sprites])
                        if style == 'player':
                            if col == '0':
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
