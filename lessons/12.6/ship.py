import pygame


class Ship():
    def __init__(self, ship_setting, screen):
        self.screen = screen
        self.setting = ship_setting

        self.image = pygame.image.load('images/ship.bmp')
        self.image_rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.image_rect.midleft = self.screen_rect.midleft

        # self.image_rect.centerx = self.screen_rect.centerx
        # self.image_rect.centery = self.screen_rect.centery

        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.image_rect.top > 0:
            self.image_rect.centery -= 1
        if self.moving_down and self.image_rect.bottom < self.screen_rect.bottom:
            self.image_rect.centery += 1

    def blitme(self):
        self.screen.blit(self.image, self.image_rect)
