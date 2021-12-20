import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    def __init__(self, star_game):
        super().__init__()
        self.screen = star_game.screen

        self.image = pygame.image.load("images/star.bmp")
        self.rect = self.image.get_rect()

        # появление звезды в левом верхем углу
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # сохранение точной горизонтальной позиции пришельца
        self.x = float(self.rect.x)


