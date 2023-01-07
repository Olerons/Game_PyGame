import pygame
from debug import debug
from settings import *
from tile import Tile
from player import Player
from helper_def import import_csv_layout

# создание и отрисовка уровня
class Level:
    def __init__(self):
        # получили главный surface с нашего display
        self.screen = pygame.display.get_surface()

        # создаем группу для спрайтов, которые будем рисовать
        self.visible_sprites = pygame.sprite.Group()
        # Создаем группу для спрайтов, которые будут препятствиями
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        # создаем карту исходя из списка в константе WORLD_MAP
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'X':
                    # наши тайлы X создаются сразу с двумя группами - так,
                    # как их надо и рисовать, и одновременно они являются препятствием
                    Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'P':
                    # игрока сохраним в переменную - в дальнейшем это понадобится
                    self.player = Player((x,y), [self.visible_sprites], self.obstacle_sprites )

    def draw(self):
        # рисуем только группу видимых спрайтов
        self.visible_sprites.draw(self.screen)
        self.visible_sprites.update()
        debug(self.player.direction)
