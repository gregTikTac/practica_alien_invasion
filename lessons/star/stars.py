import pygame

class Star:
    def __init__(self, star_game):
        self.screen = star_game.screen
        self.screen_rect = star_game.screen.get_rect()
        self.settings = star_game.settings

        self.image = pygame.image.load("images/star.bmp")
        self.image_rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.screen_rect)