import pygame
from settings import *
from helper_def import load_img

class Player(pygame.sprite.Sprite):
    # Добавляем как атрибут - группу препятствий
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = load_img('../data/test/hero.png')
        self.rect = self.image.get_rect(topleft = pos)

        # для определения направления игрока используем 2d вектор
        # по сути это кортеж (0,0) или (x,y)
        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.obstacle_sprites = obstacle_sprites

    def event_process(self):
        # получаем все нажатые кнопки
        keys = pygame.key.get_pressed()

        # если нажатая кнопка True - меняем у вектора x или y
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

    def move(self, speed):
        # эти две строчки могу объяснить по запросу
        # если кратко - для того, чтобы при движении по диагонали
        # у нас не получалась скорость в два раза выше.
        # можете закомментить их и посмотреть дебаггер - он покажет разницу
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.x += self.direction.x * speed
        self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        self.collision('vertical')

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    # если кратко - при столкновении справа мы правую сторону игрока
                    # ставим к левой стороне препятствия и наоборот
                    if self.direction.x > 0:  # Столкновение справа
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:  # Столкновение слева
                        self.rect.left = sprite.rect.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:  # Столкновение снизу
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:  # Столкновение сверху
                        self.rect.top = sprite.rect.bottom
    def update(self):
        self.event_process()
        self.move(self.speed)