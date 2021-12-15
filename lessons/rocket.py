import pygame


class Rocket():

    def __init__(self, rocket_settings, screen):
        self.screen = screen
        self.settings = rocket_settings

        self.image = pygame.image.load("img/ship.bmp")
        self.image_rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.image_rect.centerx = self.screen_rect.centerx
        self.image_rect.centery = self.screen_rect.centery

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_left and self.image_rect.left > 0:
            self.image_rect.centerx -= 1
        if self.moving_right and self.image_rect.right < self.screen_rect.right:
            self.image_rect.centerx += 1
        if self.moving_up and self.image_rect.top > 0:
            self.image_rect.centery -= 1
        if self.moving_down and self.image_rect.bottom < self.screen_rect.bottom:
            self.image_rect.centery += 1

    def blitme(self):
        self.screen.blit(self.image, self.image_rect)

