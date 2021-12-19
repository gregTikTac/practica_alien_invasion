import pygame
from settings import Settings
from stars import Star
import sys


class StarsOnTheScreen:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Star in the space")

        self.star = Star(self)

    def run_game(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.screen_cilor)
        self.star.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    game = StarsOnTheScreen()
    game.run_game()
