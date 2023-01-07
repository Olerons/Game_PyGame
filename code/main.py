import sys
import pygame
from settings import *
from level import Level
from debug import debug

# Основной класс игры
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Fantasy Game')
        # размеры окна берем из констант в settings.py
        self.game_screen = pygame.display.set_mode((WIDTH, HIGHT))

        self.running = True
        self.clock = pygame.time.Clock()

        # создаем уровень
        self.level = Level()

    def run(self):
        while self.running:

            # два метода отвечают за обработку эвентов и рендер
            self.event_process()
            self.render()

            # используем update для отрисовки обектов
            pygame.display.update()
            # FPS константа из settings.py
            self.clock.tick(FPS)

        pygame.quit()

    def event_process(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def render(self):
        self.game_screen.fill('black')

        # здесь идет отрисовка уровня
        self.level.draw()

        # специальная функция debug (debug.py), которая позволяет
        # выводить на экран отладочную информацию
        debug('Test')


if __name__ == '__main__':
    app = Game()
    app.run()
    sys.exit()
