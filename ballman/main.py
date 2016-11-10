import pygame
from pygame.sprite import Group
import sys


def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Name Game")
    # Запуск основного цикла игры.

    while True:
        # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Отображение последнего прорисованного экрана.
        pygame.display.flip()

run_game()