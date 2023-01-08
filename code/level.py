import pygame
from debug import debug
from settings import *
from tile import Tile
from player import Player
from helper_def import import_csv_layout

class Level:
    def __init__(self):
        self.screen = pygame.display.get_surface()

        # создаем специальную группу для наших "видимых" спрайтов
        # у этой группы мы сделаем свой метод draw, чтобы рисовать со смещением
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

# наследуем все свойства и методы от класса Group
class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()
        # узнаем середину экрана
        self.half_width = self.screen.get_size()[0] // 2
        self.half_height = self.screen.get_size()[1] // 2
        # создадим вектор который будет контролировать смещение отрисовки
        # про вектор можно посмотреть в предыдущих коммитах
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        # вычисляем смещение игрока относительно центра
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # перебираем и отрисовываем каждый спрайт в данной группе
        # но рисуем с учетом смещения
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.screen.blit(sprite.image, offset_pos)

