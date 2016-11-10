
import sys
import random
import pygame
from game_objects import Ball



def check_events_keydown(event, platform):
    """
     нажатие клавиш
    :param event:
    :param ship: class Ship
    """
    if event.key == pygame.K_RIGHT:
        platform.moving_right = True
    elif event.key == pygame.K_LEFT:
        platform.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_events_keyup(event, platform):
    """
    отпускание клавиш
    """
    if event.key == pygame.K_RIGHT:
        platform.moving_right = False
    elif event.key == pygame.K_LEFT:
        platform.moving_left = False



def check_events(screen, platform):
    """Обрабатывает нажатия клавиш и события мыши."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_events_keydown(event, platform)
        elif event.type == pygame.KEYUP:
            check_events_keyup(event, platform)



def create_balls(screen, image, conf, balls, platform):
    ball = Ball(screen, image, conf)
    ball.rect.left = random.randint(0, conf.width_screen - ball.rect.width)
    balls.add(ball)


def update_balls(balls, conf):
    balls.update()
    for ball in balls.copy():
        if ball.rect.top >= conf.height_screen:
            balls.remove(ball)
    print(len(balls))