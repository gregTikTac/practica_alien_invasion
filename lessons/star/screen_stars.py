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

        self.stars = pygame.sprite.Group()
        self._create_many_stars()


    def run_game(self):
        running = True
        while running:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_many_stars(self):
        star = Star(self)
        star_width, star_height = star.rect.size  # ширина звезды определяется оп атр rect
        availiable_space_x = self.settings.screen_width - (2 * star_width)  # доступное горизонтальное пространство
        number_stars_x = availiable_space_x // (2 * star_width)  # количество пришельцев
        # определяет количество рядов, помещающихся на экране
        availiable_space_y = (self.settings.screen_height - (3 * star_height))  # чтобы знать сколько вместиться рядов
        number_rows = availiable_space_y // (2 * star_height)  # количество рядов
        for row_number in range(number_rows):
            # создание первого ряда звезд
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        star = Star(self)
        star_width, star_height = star.rect.size  # создание звезды и ее координаты
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x
        star.rect.y = star.rect.height + 2 * star.rect.height * row_number
        self.stars.add(star)

    def _update_screen(self):
        self.screen.fill(self.settings.screen_color)
        self.stars.draw(self.screen)

        pygame.display.flip()


if __name__ == "__main__":
    game = StarsOnTheScreen()
    game.run_game()
