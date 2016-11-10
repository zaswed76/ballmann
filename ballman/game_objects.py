import pygame
from pygame.sprite import Group
from pygame.sprite import Sprite


class Platform:

    def __init__(self, screen, conf, image):
        """
        доска которая ловит мячик
        """
        self.image = pygame.image.load(image)
        self.conf = conf
        self.screen = screen

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Сохранение вещественной координаты центра корабля.
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_bottom = False

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_x += self.conf.platform_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center_x -= self.conf.platform_speed_factor



        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y


class Ball(Sprite):

    def __init__(self, screen, image, conf):
        """
        мячик
        :param groups:
        """
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.conf = conf
        self.screen = screen

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # новый появляется в левом верхнем углу экрана.
        self.rect.top = self.screen_rect.top
        # self.rect.x = 100
        # Сохранение точной позиции
        self.y = float(self.rect.centery)

    def blitme(self):
        """Выводит пришельца в текущем положении."""
        self.screen.blit(self.image, self.rect)

    def update(self, *args):
        self.y += self.conf.ball_speed_factor
        self.rect.centery = self.y