import pygame
from pygame.sprite import Group
import sys
import functions as gf
from config import Config
from game_objects import Ball, Platform

ball_image = 'images/ball.png'

def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    conf = Config()
    screen = pygame.display.set_mode(
        (conf.width_screen, conf.height_screen))
    pygame.display.set_caption("Name Game")

    bg = pygame.image.load("images/bg.jpg")
    platform = Platform(screen, conf, 'images/platform.png')
    balls = Group()
    gf.create_balls(screen, ball_image, conf,  balls, platform)
    # Запуск основного цикла игры.
    timer = pygame.time.Clock()
    while True:
        timer.tick(120)
        # Отслеживание событий клавиатуры и мыши.
        gf.check_events(screen, platform)

        screen.blit(bg, (0, 0))

        platform.update()
        platform.blitme()
        gf.update_balls(balls, conf, screen, ball_image, platform)
        balls.draw(screen)
        # Отображение последнего прорисованного экрана.
        pygame.display.flip()


run_game()
