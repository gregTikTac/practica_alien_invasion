import pygame
from setting import Settings
from ship import Ship
import function as func


def run_game():
    pygame.init()
    ship_settings = Settings()
    screen = pygame.display.set_mode((ship_settings.screen_width, ship_settings.screen_height))
    pygame.display.set_caption("Боковая стрельба")
    ship = Ship(ship_settings, screen)

    running = True
    while running:
        func.check_events(ship)
        ship.update()
        func.update_screen(ship_settings, screen, ship)


run_game()
