import pygame
from settings import *
from helper_def import load_img

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = load_img('../data/test/hero.png')
        self.rect = self.image.get_rect(topleft = pos)

        # добавляем хитбокс персонажу.
        # Он будет немного отличаться от
        # обычного rect этого спрайта
        # Но зато мы сможем делать более красивые
        # штуки типа "перспективы"
        # метод inflate может менять наш rect по x и y
        # (выглядит как сжатие или растяжение)
        self.hitbox = self.rect.inflate(0, -20)

        self.direction = pygame.math.Vector2()
        self.speed = 10

        self.obstacle_sprites = obstacle_sprites

    def event_process(self):
        keys = pygame.key.get_pressed()

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
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        # теперь мы фиксируем столкновения не со своим
        # спрайтом, а с его хитобоксом
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')

        # не забываем переместить центр спрайта в центр хитбокса,
        # а то у нас спрайт и хитбокс будут существовать раздельно
        self.rect.center = self.hitbox.center

    def collision(self, direction):
        # соответственно и тут мы проверяем
        # персечение не rect, а hitbox
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:  # Столкновение справа
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:  # Столкновение слева
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:  # Столкновение снизу
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:  # Столкновение сверху
                        self.hitbox.top = sprite.hitbox.bottom
    def update(self):
        self.event_process()
        self.move(self.speed)