import pygame
import sys
from settings import Settings


class InitPractica():
    """класс для упраления русурсами и поведением игры"""

    def __init__(self):
        """инициализирует угру и создает игровые ресурсы"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((1200, 800))  # размер экрана
        pygame.display.set_caption("Практика")  # верхня часть окна с названием

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()  # вызов вспомогательного _метода
            self._update_screen()  # вызов вспомогательного _метода


    def _check_events(self):
        for event in pygame.event.get():  #  отслеживание событий клавиатуры и мыши
            if event.type == pygame.QUIT:
                sys.exit()


    def _update_screen(self):
        """Обновляет изображение на экране и отображает новый экран"""
        self.screen.fill(self.settings.bg_color)  # при каждом проходе цикла переписывает экран

        pygame.display.flip()  # отображение последнего прорисованного экрана


