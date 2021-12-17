import sys
import pygame


def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            _check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            _check_keyup_events(event, ship)


def _check_keydown_events(event, ship):
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True


def _check_keyup_events(event, ship):
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def update_screen(game_settings, screen, ship):
    screen.fill(game_settings.color)
    ship.blitme()
    pygame.display.flip()
