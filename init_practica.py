import pygame
import sys
from settings import Settings


class InitPractica():
    """класс для упраления русурсами и поведением игры"""

    def __init__(self):
        """инициализирует угру и создает игровые ресурсы"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))  # атрибуты для создания экрана
        pygame.display.set_caption("Практика")  # верхня часть окна с названием

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()  # вызов вспомогательного _метода
            self._update_screen()  # вызов вспомогательного _метода

    def _check_events(self):
        for event in pygame.event.get():  # отслеживание событий клавиатуры и мыши
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Обновляет изображение на экране и отображает новый экран"""
        self.screen.fill(self.settings.bg_color)  # при кажд проходе цикла переписывает экран(для получения цвета фона)

        pygame.display.flip()  # отображение последнего прорисованного экрана


if __name__ == "__main__":
    game_pr = InitPractica()  # экземпляр игры
    game_pr.run_game()  # вызов метода
