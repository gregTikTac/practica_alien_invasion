import pygame
from settings import Settings
from rocket import Rocket
import functions as f


def run():
    pygame.init()
    rocket_settings = Settings()
    screen = pygame.display.set_mode((rocket_settings.screen_width, rocket_settings.screen_height))
    pygame.display.set_caption("Rocket")
    rocket = Rocket(rocket_settings, screen)

    running = True
    while running:
        f.check_events(rocket)
        rocket.update()
        f.update_screen(rocket_settings, screen, rocket)


run()
