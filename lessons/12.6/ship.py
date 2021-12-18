import pygame


class Ship:
    def __init__(self, setting_game):
        self.screen = setting_game.screen
        self.settings = setting_game.settings

        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = setting_game.screen.get_rect()
        self.rect.midleft = self.screen_rect.midleft

        self.x = float(self.rect.x)

        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= self.settings.speed_ship
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.settings.speed_ship
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
