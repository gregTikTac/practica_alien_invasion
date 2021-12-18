import sys
import pygame
from settings import Settings
from ship import Ship
from  bullets import Bullets


class InitGame:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("side shooting")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.screen_rect = self.screen.get_rect() # края экрана

    def run_game(self):
        running = True
        while running:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            # удаление снарядов
            for bullet in self.bullets.copy():
                if bullet.rect.right >= self.screen_rect.right: # если снаряд вышел за правый край
                    self.bullets.remove(bullet) # то удаляем его
            print(len(self.bullets))

            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullets(self):
        new_bullets = Bullets(self)
        self.bullets.add(new_bullets)

    def _update_screen(self):
        self.screen.fill(self.settings.color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()


if __name__ == "__main__":
    ig = InitGame()
    ig.run_game()